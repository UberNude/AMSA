import re, time, unicodedata, hashlib, types, os, inspect, datetime, common, tvdb, anidb, urllib
from common import Common
#from Common import CommonStart, XMLFromURL, SaveFile, MapSeries, GetElementText
from dateutil.parser import parse as dateParse
from lxml import etree
from lxml.builder import E
from lxml.etree import Element, SubElement, Comment
          
### Pre-Defined Start function #########################################################################################################################################
def Start():
    Log.Debug('--- AmsaTVAgentTest Start -------------------------------------------------------------------------------------------')
    #common = Common()
    #common.CommonStart()


### Pre-Defined ValidatePrefs function Values in "DefaultPrefs.json", accessible in Settings>Tab:Plex Media Server>Sidebar:Agents>Tab:Movies/TV Shows>Tab:AmsaTV #######
def ValidatePrefs(): #     a = sum(getattr(t, name, 0) for name in "xyz")
    DefaultPrefs = ("GetTvdbFanart", "GetTvdbPosters", "GetTvdbBanners", "GetAnidbPoster", "localart", "adult", 
                  "GetPlexThemes", "MinimumWeight", "SerieLanguage1", "SerieLanguage2", "SerieLanguage3", 
                  "AgentPref1", "AgentPref2", "AgentPref3", "EpisodeLanguage1", "EpisodeLanguage2")
    try: [Prefs[key] for key in DefaultPrefs]
    except: Log.Error("Init - ValidatePrefs() - DefaultPrefs.json invalid" );  return MessageContainer ('Error', "Value '%s' missing from 'DefaultPrefs.json', update it" % key)
    else: Log.Info ("Init - ValidatePrefs() - DefaultPrefs.json is valid");  return MessageContainer ('Success', 'AMSA - Provided preference values are ok')
  
  
### Agent declaration ###############################################################################################################################################
class AmsaTVAgentTest(Agent.TV_Shows):    
    name = 'Anime Multi Source Agent (Test)'
    primary_provider = True
    fallback_agent = False
    contributes_to = None
    languages = [Locale.Language.English]
    accepts_from = ['com.plexapp.agents.localmedia'] 
    
    def search(self, results, media, lang, manual=False):
        Log.Debug('--- Search Begin -------------------------------------------------------------------------------------------')
        common = Common()
        orig_title = unicodedata.normalize('NFC', unicode(media.show)).strip().replace("`", "'")
        if orig_title.startswith("clear-cache"):   HTTP.ClearCache()
        Log.Info("Init - Search() - Title: '%s', name: '%s', filename: '%s', manual:'%s'" % (orig_title, media.name, urllib.unquote(media.filename) if media.filename else '', str(manual)))
               
        match = re.search("(?P<show>.*?) ?\[(?P<source>(.*))-(tt)?(?P<id>[0-9]{1,7})\]", orig_title, re.IGNORECASE)
        if match:
            show = match.group('show')
            source = match.group('source').lower() 
            if source in ["anidb", "tvdb"]:
                id = match.group('id')
                startdate = None
                if source=="anidb":  
                    show = anidb.getAniDBTitle(common.AniDB_title_tree.xpath("/animetitles/anime[@aid='%s']/*" % id))
                Log.Debug("Init - Search() - force - id: '%s-%s', show from id: '%s' provided in foldername: '%s'" % (source, id, show, orig_title) )
                results.Append(MetadataSearchResult(id="%s-%s" % (source, id), name=show, year=startdate, lang=Locale.Language.English, score=100))
                return
            else: orig_title = show
       
        maxi = {}
        elite = []
        @parallelize
        def searchTitles():
            for anime in common.AniDB_title_tree.xpath("""./anime/title
                [@type='main' or @type='official' or @type='syn' or @type='short']
                [translate(text(),"ABCDEFGHJIKLMNOPQRSTUVWXYZ 0123456789.`", "abcdefghjiklmnopqrstuvwxyz 0123456789.'")="%s"
                or contains(translate(text(),"ABCDEFGHJIKLMNOPQRSTUVWXYZ 0123456789.`", "abcdefghjiklmnopqrstuvwxyz 0123456789.'"),"%s")]""" % (orig_title.lower().replace("'", "\'"), orig_title.lower().replace("'", "\'"))):
                @task
                def scoreTitle(anime=anime, maxi=maxi):
                    element = anime.getparent()
                    id = element.get('aid')
                    if not id in maxi: 
                        title = anime.text
                        langTitle = anidb.getAniDBTitle(element)
                        if title == orig_title.lower():
                            score = 100
                        elif langTitle == orig_title.lower():
                            score = 100
                        else:   
                            score = 100 * len(orig_title) / len(langTitle)
                        
                        isValid = True
                        if id in maxi and maxi[id] <= score:
                            isValid = False
                        else: 
                            maxi[id] = score
                        startdate = None
                        if(media.year and score >= 90 and isValid):
                            try: data = common.XMLFromURL(anidb.ANIDB_HTTP_API_URL + id, id+".xml", "AniDB\\" + id, CACHE_1HOUR * 24).xpath('/anime')[0]
                            except: Log.Error("Init - Search() - AniDB Series XML: Exception raised, probably no return in xmlElementFromFile") 
                            if data: 
                                try: startdate = dateParse(common.GetElementText(data, 'startdate')).year
                                except: pass
                                if str(startdate) != str(media.year):
                                    isValid = False 
                                Log.Debug("Init - Search() - date: '%s', aired: '%s'" % (media.year, startdate)) 
                            elite.append(isValid)
                        elif score >= 90 and isValid:
                            elite.append(isValid)
                        if isValid: 
                            Log.Debug("Init - Search() - find - id: '%s-%s', title: '%s', score: '%s'" % ("anidb", id, langTitle, score))
                            results.Append(MetadataSearchResult(id="%s-%s" % ("anidb", id), name="%s [%s-%s]" % (langTitle, "anidb", id), year=startdate, lang=Locale.Language.English, score=score))
            
        if len(elite) > 0 and not True in elite: del results[:]
        results.Sort('score', descending=True)
        return
        
    ### Parse the AniDB anime title XML ##################################################################################################################################
    def update(self, metadata, media, lang, force=False):
        Log.Debug('--- Update Begin -------------------------------------------------------------------------------------------')
        common = Common()
        source, id = metadata.id.split('-')     
        
        mappingData = None
        if source == "anidb": 
            anidbid = id
            mappingData = common.AniDB_TVDB_mapping_tree.xpath("""./anime[@anidbid="%s"]""" % (anidbid))[0]
            if mappingData:
                tvdbid = mappingData.get('tvdbid')
        if source == "tvdbid": 
            tvdbid = id
            mappingData = common.AniDB_TVDB_mapping_tree.xpath("""./anime[@tvdbid="%s"]""" % (tvdbid))[0]
            if mappingData:
                anidbid = mappingData.get('anidbid')  
        Log.Debug("Init - Update() - source: '%s', anidbid: '%s', tvdbid: '%s'" % (source, anidbid, tvdbid))
        
        mappingXml = common.AniDB_TVDB_mapping_tree.xpath("""./anime[@tvdbid="%s"]""" % (tvdbid))
        map = common.MapSeries(media, mappingXml)
        
        for mappedSeries in common.AniDB_TVDB_mapping_tree.xpath("""./anime[@tvdbid="%s"]""" % (tvdbid)):
            anidbid_season = mappedSeries.get('anidbid')
            Log.Debug("Init - Update() - anidbid_season: '%s', tvdbid: '%s'" % (anidbid_season, tvdbid))
            #series = map.xpath("""./Season[@num="%s"]""" % (mappedSeries.get('defaulttvdbseason')))[0]
            #if series:
            #    series.set("anidbid", anidbid)
            #    series.set("tvdbid", tvdbid)
        
        common.SaveFile(etree.tostring(map, pretty_print=True, xml_declaration=True, encoding='UTF-8'), id + ".bundle.xml", "Bundles\\")
        
        #anidb. populateMetadata(anidbid, mappingData)

    
