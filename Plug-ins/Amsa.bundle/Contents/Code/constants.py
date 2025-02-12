from string import maketrans 

#-------------------AMSA-------------------#
BaseDirectory = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "..", "..", "..", "..", "Plug-in Support", "Data", "com.plexapp.agents.amsa", "DataItems"))
CacheDirectory = "Cache"
CachePath = os.path.join(BaseDirectory, CacheDirectory)
BundleExportDirectory = "Export"
BundleExportPath = os.path.join(BaseDirectory, BundleExportDirectory)
DefaultTimeout = 30
DefaultCache = CACHE_1HOUR * 24 * 2
ReplaceChars = maketrans("`", "'")
StreamTypes = {1: "video", 2: "audio", 3: "subtitle"}
SeriesAttribs = ["Title", "Summary", "Originally_Available_At", "Rating", "Studio", "Countries", "Duration", "Genres", "Tags", "Collections", "Content_Rating", "Writers", "Directors", "Producers", "Roles", "Art", "Posters", "Banners", "Season", "Themes", "Links"]
EpisodeAttribs = ["Title", "Summary", "Originally_Available_At", "Rating", "Absolute_Index", "Writers", "Directors", "Producers", "Thumbs"]
ExportBundles = False
FILTER_SEARCH_WORDS  = ['to', 'wa', 'ga', 'no', 'age', 'da', 'chou', 'super', 'yo', 'de', 'chan', 'hime', 'ni', 'sekai',                                                                    # Jp
                        'a',  'of', 'an', 'the', 'motion', 'picture', 'special', 'oav', 'ova', 'tv', 'special', 'eternal', 'final', 'last', 'one', 'movie', 'me',  'princess', 'theater',   # En Continued
                        'le', 'la', 'un', 'les', 'nos', 'vos', 'des', 'ses',                                                                                                                # Fr
                        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi']                                                               # Roman digits
Filter_Regex = r'\b' + r'\b|\b'.join(map(re.escape, FILTER_SEARCH_WORDS)) + r'\b'
Default_headers = {"Accept-Encoding":"gzip, deflate", "content-type":"charset=utf8", "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

SERIES_LANGUAGE_PRIORITY                    = [Prefs["SerieLanguage1"].encode("utf-8"), Prefs["SerieLanguage2"].encode("utf-8"), Prefs["SerieLanguage3"].encode("utf-8"), "main"]  
EPISODE_LANGUAGE_PRIORITY                   = [Prefs["EpisodeLanguage1"].encode("utf-8"), Prefs["EpisodeLanguage2"].encode("utf-8")]                                              
SERIES_TITLE_PRIORITY                       = [item.lower() for item in Prefs["SeriesTitle"].encode("utf-8").split(',')] 
SERIES_SUMMARY_PRIORITY                     = [item.lower() for item in Prefs["SeriesSummary"].encode("utf-8").split(',')] 
SERIES_ORIGINALLYAVAILABLEAT_PRIORITY       = [item.lower() for item in Prefs["SeriesOriginally_Available_At"].encode("utf-8").split(',')] 
SERIES_RATING_PRIORITY                      = [item.lower() for item in Prefs["SeriesRating"].encode("utf-8").split(',')] 
SERIES_STUDIO_PRIORITY                      = [item.lower() for item in Prefs["SeriesStudio"].encode("utf-8").split(',')] 
SERIES_COUNTRIES_PRIORITY                   = [item.lower() for item in Prefs["SeriesCountries"].encode("utf-8").split(',')] 
SERIES_DURATION_PRIORITY                    = [item.lower() for item in Prefs["SeriesDuration"].encode("utf-8").split(',')] 
SERIES_GENRES_PRIORITY                      = [item.lower() for item in Prefs["SeriesGenres"].encode("utf-8").split(',')] 
SERIES_TAGS_PRIORITY                        = [item.lower() for item in Prefs["SeriesTags"].encode("utf-8").split(',')] 
SERIES_COLLECTIONS_PRIORITY                 = [item.lower() for item in Prefs["SeriesCollections"].encode("utf-8").split(',')] 
SERIES_CONTENTRATING_PRIORITY               = [item.lower() for item in Prefs["SeriesContent_Rating"].encode("utf-8").split(',')] 
SERIES_WRITERS_PRIORITY                     = [item.lower() for item in Prefs["SeriesWriters"].encode("utf-8").split(',')] 
SERIES_DIRECTORS_PRIORITY                   = [item.lower() for item in Prefs["SeriesDirectors"].encode("utf-8").split(',')] 
SERIES_PRODUCERS_PRIORITY                   = [item.lower() for item in Prefs["SeriesProducers"].encode("utf-8").split(',')] 
SERIES_ROLES_PRIORITY                       = [item.lower() for item in Prefs["SeriesRoles"].encode("utf-8").split(',')]
SERIES_IMAGES_PRIORITY                      = [item.lower() for item in Prefs["SeriesImages"].encode("utf-8").split(',')]
SERIES_THEMES_PRIORITY                      = [item.lower() for item in Prefs["SeriesThemes"].encode("utf-8").split(',')]
EPISODE_TITLE_PRIORITY                      = [item.lower() for item in Prefs["EpisodeTitle"].encode("utf-8").split(',')] 
EPISODE_SUMMARY_PRIORITY                    = [item.lower() for item in Prefs["EpisodeSummary"].encode("utf-8").split(',')] 
EPISODE_ORIGINALLYAVAILABLEAT_PRIORITY      = [item.lower() for item in Prefs["EpisodeOriginally_Available_At"].encode("utf-8").split(',')] 
EPISODE_RATING_PRIORITY                     = [item.lower() for item in Prefs["EpisodeRating"].encode("utf-8").split(',')] 
EPISODE_ABSOLUTE_INDEX_PRIORITY             = [item.lower() for item in Prefs["EpisodeAbsolute_Index"].encode("utf-8").split(',')] 
EPISODE_WRITERS_PRIORITY                    = [item.lower() for item in Prefs["EpisodeWriters"].encode("utf-8").split(',')] 
EPISODE_DIRECTORS_PRIORITY                  = [item.lower() for item in Prefs["EpisodeDirectors"].encode("utf-8").split(',')] 
EPISODE_PRODUCERS_PRIORITY                  = [item.lower() for item in Prefs["EpisodeProducers"].encode("utf-8").split(',')] 
EPISODE_THUMBS_PRIORITY                     = [item.lower() for item in Prefs["EpisodeThumbs"].encode("utf-8").split(',')]
#-------------------AMSA-------------------#

#-------------------ANIDB------------------#
ANIDB_TITLES                                = "http://anidb.net/api/anime-titles.xml"   
ANIDB_HTTP_API_URL                          = "http://api.anidb.net:9001/httpapi?request=anime&client=amsa&clientver=1&protover=1&aid="            
ANIDB_IMAGE_DOMAIN                          = "https://cdn.anidb.net/"
ANIDB_PIC_BASE_URL                          = "images/main/"
ANIDB_PIC_THUMB_URL                         = "images/150/%s.jpg-thumb.jpg"

ANIDB_RESOURCES_ANN                         = "http://www.animenewsnetwork.com/encyclopedia/anime.php?id=%s"
ANIDB_RESOURCES_MAL                         = "http://myanimelist.net/anime/%s"
ANIDB_RESOURCES_ANIMENFO                    = "http://www.animenfo.com/animetitle,%s,%s,a.html"
ANIDB_RESOURCES_WIKIEN                      = "http://en.wikipedia.org/wiki/%s"
ANIDB_RESOURCES_WIKIJP                      = "http://ja.wikipedia.org/wiki/%s"
ANIDB_RESOURCES_SCHEDULE                    = "http://cal.syoboi.jp/tid/%s/time"
ANIDB_RESOURCES_ALLCINEMA                   = "http://www.allcinema.net/prog/show_c.php?num_c=%s"
ANIDB_RESOURCES_ANISON                      = "http://anison.info/data/program/%s.html"
ANIDB_RESOURCES_LAIN                        = "http://lain.gr.jp/%s"
ANIDB_RESOURCES_VNDB                        = "http://vndb.org/v%s"
ANIDB_RESOURCES_MARUMEGANE                  = "http://www.anime.marumegane.com/%s.html"
ANIDB_RESOURCES_HOMEAKI                     = "http://home-aki.cool.ne.jp/anime-list/%s.htm"

MINIMUM_WEIGHT                              = Prefs["MinimumWeight"]
SERIES_TYPE_PRIORITY                        = ["official", "main", "syn", "synonym", "short"]
ANIDB_THROTTLE_THRESHOLD                    = 100
ANIDB_ANTIBAN_WAIT                          = int(Prefs["AniDbAntiBanDelay"]) if int(Prefs["AniDbAntiBanDelay"]) > 2 else 2
ANIDB_BADTITLES                             = ["^TV Special$", "^Part . of .$", "^Episode [S]?.$", "^Special [S]?.$", "Complete Movie"]

SEARCH_USE_ANIDB                             = Prefs["UseAniDBForAdvancedSearch"]
#-------------------ANIDB------------------#

#-------------------TVDB-------------------#
TVDB_HTTP_API_URL                           = "http://thetvdb.com/api/DC6295EB0E09E931/series/%s/all/en.xml"                                   
TVDB_BANNERS_URL                            = "http://thetvdb.com/api/DC6295EB0E09E931/series/%s/banners.xml"                                 
TVDB_SERIE_SEARCH                           = "http://thetvdb.com/api/GetSeries.php?seriesname="                                                 
TVDB_IMAGES_URL                             = "http://thetvdb.com/banners/"                                                                    
TVDB_SERIE_URL                              = "http://thetvdb.com/?tab=series&id=%s"  

SEARCH_USE_TVDB                             = Prefs["UseTVDBForAdvancedSearch"]
#-------------------TVDB-------------------#

#-------------------ANIME-LISTS------------#
ANIDB_TVDB_MAPPING                          = "https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml"                                                                                
ANIDB_COLLECTION                            = "https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-movieset-list.xml"
ANIDB_TVDB_MAPPING_CUSTOM                   = os.path.join(CacheDirectory, "anime-list-custom.xml")
ANIDB_TVDB_MAPPING_CORRECTIONS              = "https://raw.githubusercontent.com/Dingmatt/AMSA/master/Plug-in%20Support/Data/com.plexapp.agents.amsa/DataItems/Cache/anime-list-corrections.xml"  
#-------------------ANIME-LISTS------------#

#-------------------PLEX-------------------#
THEME_URL                                   = 'http://tvthemes.plexapp.com/%s.mp3'        
#-------------------PLEX-------------------#

#-------------------MYANIMELIST------------#
MAL_HTTP_API_URL                            = "http://fribbtastic-api.net/fribbtastic-api/services/anime?id="
MAL_PREFIX                                  = "https://myanimelist.cdn-dena.com"      
#-------------------MYANIMELIST------------#

class Series():
    ID = None
    MetaType = None
    Title = None
    Summary = None
    Originally_Available_At = None
    Rating = None
    Studio = None
    Countries = None
    Duration = None
    Genres = None
    Tags = None
    Collections = None
    Content_Rating = None
    Writers = None
    Directors = None
    Producers = None
    Roles = None
    Art = None
    Posters = None
    Banners = None
    Season = None
    Themes = None
    EpisodeCount = None
    SpecialCount = None
    OpList = None
    EdList = None
    Episodes = None
    Links = None
    
class Episode():
    Title = None
    Summary = None
    Originally_Available_At = None
    Rating = None
    Absolute_Index = 0
    Writers = None
    Directors = None
    Producers = None
    Thumbs = None
    Number = None
    Season = None