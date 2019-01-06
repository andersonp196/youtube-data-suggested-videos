import json
import requests
import random
import sys
import csv
from datetime import datetime
import math
import re

apiKey = 'YOURAPIKEYGOESHERE

#Options
#sequence = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765],[1,2,4,8,16,32,64,128,256,512,1024,2048,8192,16384,32768,65536,131072,262144,524288]]
#sequence = [[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10],[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4],['random']]
sequence = [[2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5,2,3,5,3]]
#start_videos = [['-ukNDmmTOLM','a3JgESVHJu0','cEc7ZuHyKWE','kHLHSlExFis','DiaDblUd-lw','4uh9vFwFo3c','SsKT0s5J8ko','ANohtXQhkQw','zdf2seAVZ_g','RQTgJRwMdKQ','wdER__ZSmHg','v8wh2AJPbPM','fwijCB6cH-0','BSL7l2Ie_NY','MdirPsiHnCA','52WMEYtpHi0','u3ePPA0yzSU','OQKAEjPIDNk','B6IlQ7UYeEM','qBlEtLWtNzw','wnqjSgMU36U','rAqMlh0b2HU','T2sO8gK2IKk','DwDVd0SxDiw','iUaI-PO3btQ','ceb7otlOqNk','wlDhSyubX4o','WuDy1XOU6_E','UOUBW8bkjQ4','fhlWTEOH2so','kvfqMOyJDQY','s6nJTmr-ntY','diLp6hUqvVk','gR1owF4sIqI','fbNDJRwXKGc','B8-FlvLjplg','e0H3WC3Ahgk','K7VhlE23W30','gi_2GELMwfY','wgbV6DLVezo','7wnN0AQRyRY','rijvxtrhsUI','9K_OzUtiEbY','s05ixiBStRY','5MsOON5lkzU','c_8U7gjb2k4','WqxYyUR72jU','GxFk9-IyAa4','fAkjKzfzBLE','osd5HhjDt6A','ceb7otlOqNk','wlDhSyubX4o','WuDy1XOU6_E','UOUBW8bkjQ4','fhlWTEOH2so','kvfqMOyJDQY','s6nJTmr-ntY','diLp6hUqvVk','gR1owF4sIqI','fbNDJRwXKGc','B8-FlvLjplg','e0H3WC3Ahgk','K7VhlE23W30','gi_2GELMwfY','wgbV6DLVezo','7wnN0AQRyRY','rijvxtrhsUI','9K_OzUtiEbY','s05ixiBStRY','5MsOON5lkzU','c_8U7gjb2k4','WqxYyUR72jU','GxFk9-IyAa4','fAkjKzfzBLE','osd5HhjDt6A','akuGzIdj0rs','NOeZtQhbDwg','4wszzgOnJ5U','V1nMei4XL5s','UUgeqotr-a8','b5kwtJkUdpA','rSM8OOjaiMQ','QezxYUfW_Sk','EQnk-h-LCpQ','fJswyZkqFvc','QYjG5SVjd7E','03q3UG_3TrM','J6oy60zsrPs','lCI6LheXwis','jBHDxdcp9Mc','1hYCv24Ed3M','Els_GCWuJVk','UHqJy8P4Gb4','vHQWsQwqqvg','QuTE12qGmz8','T3WtuIddokQ','BPl7D20F2mE','-ooesGSk4b0','yUif6C_uJgk','4GihAbGZPwQ'],
               # ['kJQP7kiw5Fk','RgKAFK5djSk','JGwWNGJdvx8','9bZkp7q19f0','OPf0YbXqDm0','fRh_vgS2dFE','09R8_2nJtjg','nfWlot6h_JM','CevxZvSJLk8','NUsoVlDFqZg','lp-EO5I60KA','YQHsXMglC9A','0KSOMA3QBU0','YqeW9_5kURI','hT_nvWreIhg','e-ORhEE9VVg','6Mgqbai3fKo','7PCkvCPvDXk','HP-MbfHFUqs','PT2_F-1esPk','pRpeEdMmmQ0','RBumgq5yVrA','kffacxfA7G4','wnJ6LuUFpMo','2vjPBrBU-TM','3AtDnEC4zak','60ItHLz5WEA','AJtDXIazrMo','IcrbM1l_BoI','uelHwf8o7_U','vjW8wmF5VWc','L0MK7qz13bU','KQ6zr6kCPj8','XqZsoesa55w','TyHvyGVs42U','VqEbCxg2bNI','iOe6dI2JhgU','uxpDa-c-4Mc','fLexgOxsZu0','pXRviuL6vMY','t_jHrUE5IOk','oyEuk8j8imI','QFs3PIZb3js','34Na4j8AVgA','rYEDA3JcQqw','k2qgadSvNyU','PMivT7MJ41M','k85mRPqvMbE','GMFewiplIbw','AMTAQ-AJS4Y','t4H_Zoh7G5A','2Vv-BfVoq4g','QcIy9NiNbmo','HCjNJDNzw8Y','ASO_zypdnsQ','-UV0QGLmYys','LjhCEhWiKXk','hXI8RQYC36Q','NGLxoKOvzu4','QGJuMBdaqIw','8UVNT4wvIGY','VMp55KH_3wo','8SbUC-UaAxE','CvKgP6Ei-U8','foE1mO2yM04','YykjpeuMNEk','1G4isv_Fylg','KWZGAExj-es','sGIm0-dQd8M','qrO4YZeyl0I','Bznxx12Ptl0','ktvTqknDobU','KEI4qSrkPAs','o3mP3mJDL2k','hq3yfQnllfQ','OpQFFLBMEPI','QtXby3twMmI','3xqqj9o7TgA','9jI-z9QN6g8','jGflUbPQfW8','Km4BayZykwE','kTHNpusq654','fKopy74weus','wfWkmURBNv8','J_ub7Etch2U','nfs8NYg7yQM','tFoUuFq3vHw','CUYrEiymUMY','CTFtOOh47oo','FzG4uDgje3M','nxtIRArhVD4','HoWJeHL3AEk','jySrwZc4sZo','hoIWtgQ3Wz4','fmB95Bu-D3Q','V15BYnSr0P8','YlaWGd1cUms','uxEFermaeec','RtU_mdL2vBM','iAeYPfrXwk4']]
#PROGRAM stopped after certain point need to run from points below
start_videos = [['QYjG5SVjd7E','03q3UG_3TrM','J6oy60zsrPs','lCI6LheXwis','jBHDxdcp9Mc','1hYCv24Ed3M','Els_GCWuJVk','UHqJy8P4Gb4','vHQWsQwqqvg','QuTE12qGmz8','T3WtuIddokQ','BPl7D20F2mE','-ooesGSk4b0','yUif6C_uJgk','4GihAbGZPwQ'],
                ['kJQP7kiw5Fk','RgKAFK5djSk','JGwWNGJdvx8','9bZkp7q19f0','OPf0YbXqDm0','fRh_vgS2dFE','09R8_2nJtjg','nfWlot6h_JM','CevxZvSJLk8','NUsoVlDFqZg','lp-EO5I60KA','YQHsXMglC9A','0KSOMA3QBU0','YqeW9_5kURI','hT_nvWreIhg','e-ORhEE9VVg','6Mgqbai3fKo','7PCkvCPvDXk','HP-MbfHFUqs','PT2_F-1esPk','pRpeEdMmmQ0','RBumgq5yVrA','kffacxfA7G4','wnJ6LuUFpMo','2vjPBrBU-TM','3AtDnEC4zak','60ItHLz5WEA','AJtDXIazrMo','IcrbM1l_BoI','uelHwf8o7_U','vjW8wmF5VWc','L0MK7qz13bU','KQ6zr6kCPj8','XqZsoesa55w','TyHvyGVs42U','VqEbCxg2bNI','iOe6dI2JhgU','uxpDa-c-4Mc','fLexgOxsZu0','pXRviuL6vMY','t_jHrUE5IOk','oyEuk8j8imI','QFs3PIZb3js','34Na4j8AVgA','rYEDA3JcQqw','k2qgadSvNyU','PMivT7MJ41M','k85mRPqvMbE','GMFewiplIbw','AMTAQ-AJS4Y','t4H_Zoh7G5A','2Vv-BfVoq4g','QcIy9NiNbmo','HCjNJDNzw8Y','ASO_zypdnsQ','-UV0QGLmYys','LjhCEhWiKXk','hXI8RQYC36Q','NGLxoKOvzu4','QGJuMBdaqIw','8UVNT4wvIGY','VMp55KH_3wo','8SbUC-UaAxE','CvKgP6Ei-U8','foE1mO2yM04','YykjpeuMNEk','1G4isv_Fylg','KWZGAExj-es','sGIm0-dQd8M','qrO4YZeyl0I','Bznxx12Ptl0','ktvTqknDobU','KEI4qSrkPAs','o3mP3mJDL2k','hq3yfQnllfQ','OpQFFLBMEPI','QtXby3twMmI','3xqqj9o7TgA','9jI-z9QN6g8','jGflUbPQfW8','Km4BayZykwE','kTHNpusq654','fKopy74weus','wfWkmURBNv8','J_ub7Etch2U','nfs8NYg7yQM','tFoUuFq3vHw','CUYrEiymUMY','CTFtOOh47oo','FzG4uDgje3M','nxtIRArhVD4','HoWJeHL3AEk','jySrwZc4sZo','hoIWtgQ3Wz4','fmB95Bu-D3Q','V15BYnSr0P8','YlaWGd1cUms','uxEFermaeec','RtU_mdL2vBM','iAeYPfrXwk4']]
video_ids = []
video_titles = []
page_infos = []
current_data = []
over_max = [3,3,3]
#prev_suggestions = {}
set_names = ["set: 100 trending as of 7/14/2018", "set: 100 most viewed videos as of 7/14/2018"]
#repeat = int(input("Allow suggestions to be picked multiple times? (no-0/yes-1): "))"""
#print("\n\n\n")

def since_epoch(date):
    utc_dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = (utc_dt - datetime(1970, 1, 1)).total_seconds()
    return timestamp

def get_csv_data(data, x, j):
    try:
        publishedAt = data['snippet']['publishedAt']
    except:
        publishedAt = "unknown"
    try:
        since_epoch = since_epoch(data['snippet']['publishedAt'])
    except:
        since_epoch = "unknown"
    try:
        title = data['snippet']['title']
    except:
        title = "unknown"
    try:
        description = data['snippet']['description']
    except:
        description = "unknown"
    try:
        channelTitle = data['snippet']['channelTitle']
    except:
        channelTitle = "unknown"
    try:
        tags = data['snippet']['tags']
    except:
        tags = "unknown"
    try:
        categoryId = data['snippet']['categoryId']
    except:
        categoryId = "unknown"
    try:
        liveBroadcastContent = data['snippet']['liveBroadcastContent']
    except:
        liveBroadcastContent = "unknown"
    try:
        duration = get_seconds(data['contentDetails']['duration'])
    except:
        duration = "unknown"
    try:
        dimension = data['contentDetails']['dimension']
    except:
        dimension = "unknown"
    try:
        definition = data['contentDetails']['definition']
    except:
        definition = "unknown"
    try:
        caption = data['contentDetails']['caption']
    except:
        caption = "unknown"
    try:
        licensedContent = data['contentDetails']['licensedContent']
    except:
        licensedContent = "unknown"
    try:
        projection = data['contentDetails']['projection']
    except:
        projection = "unknown"
    try:
        viewCount = data['statistics']['viewCount']
    except:
        viewCount = "unknown"
    try:
        likeCount = data['statistics']['likeCount']
    except:
        likeCount = "unknown"
    try:
        dislikeCount = data['statistics']['dislikeCount']
    except:
        dislikeCount = "unknown"
    try:
        favoriteCount = data['statistics']['favoriteCount']
    except:
        favoriteCount = "unknown"
    try:
        commentCount = data['statistics']['commentCount']
    except:
        commentCount = "unknown"
    try:
        topicCategories = data['topicDetails']['topicCategories']
    except:
        topicCategories = "unknown"
    try:
        title_len = len(data['snippet']['title'])
    except:
        title_len = "unknown"
    try:
        desc_len = len(data['snippet']['description'])
    except:
        desc_len = "unknown"
    try:
        channelTitle_len = len(data['snippet']['channelTitle'])
    except:
        channelTitle_len = "unknown"
    try:
        tab_len = len(data['snippet']['tags'])
    except:
        tab_len = "unknown"
    if (x == 0):
        seq = 'start'
    else:
        try:
            seq = sequence[x-1]
        except:
            seq = 'random'

    return [x, sequence[j], str(mod_sequence), video_ids[x], publishedAt, since_epoch, title, description, channelTitle, tags, categoryId,
            liveBroadcastContent, duration, dimension, definition, caption, licensedContent, projection, viewCount, likeCount, dislikeCount,
            favoriteCount, commentCount, topicCategories, title_len, desc_len, channelTitle_len, tab_len, category_list[categoryId], seq, over_max[j]]
        
def get_data(video_id, per_page, page_token):
    url = 'https://www.googleapis.com/youtube/v3/search?fields=nextPageToken,pageInfo,items(id(videoId),snippet(title))&part=snippet&relatedToVideoId=' + str(video_id) + '&maxResults=' + str(per_page) + '&pageToken=' + page_token + '&type=video&regionCode=US&key=' + apiKey
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def get_all_data(video_id):
    url = 'https://www.googleapis.com/youtube/v3/videos?fields=items(id,statistics,topicDetails(topicCategories),contentDetails,snippet(title,publishedAt,description,channelTitle,tags,categoryId,liveBroadcastContent))&part=snippet,id,contentDetails,topicDetails,statistics&id=' + str(video_id) + '&type=video&key=' + apiKey
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def get_seconds(dur):
    dur = dur.replace("PT", "")
    if (dur == 0 or dur == "0"):
        return "live"
    if "H" in dur:
        if "M" not in dur:
            dur = dur.replace("S", "")
            dur = re.split("H|M",dur)
            dur = (int(dur[0])*3600)++int(dur[1])
        elif "S" in dur:
            dur = dur.replace("S", "")
            dur = re.split("H|M",dur)
            dur = (int(dur[0])*3600)+(int(dur[1])*60)+int(dur[2])
    else:
        dur = dur.replace("S", "")
        dur = dur.split("M")
        dur = (int(dur[0])*60)+int(dur[1])
    return dur

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

category_list = {'1':'Film & Animation', '2':'Autos & Vehicles', '10':'Music', '15':'Pets & Animals', '17':'Sports', '18':'Short Movies', '19':'Travel & Events',
                 '20':'Gaming', '21':'Videoblogging', '22':'People & Blogs', '23':'Comedy', '24':'Entertainment', '25':'News & Politics', '26':'Howto & Style',
                 '27':'Education', '28':'Science & Technology', '29':'Nonprofits & Activism', '30':'Movies', '31':'Anime/Animation', '32':'Action/Adventure',
                 '33':'Classics', '34':'Documentary', '35':'Documentary', '36':'Drama', '37':'Family', '38':'Foreign', '39':'Horror', '40':'Sci-Fi/Fantasy',
                 '41':'Thriller', '42':'Shorts', '43':'Shows', '44':'Trailers'}

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for k in range(0, len(set_names)):
    for j in range(0, len(start_videos)):
        orig_sequence = str(sequence[j])
        mod_sequence = []
        for l in range(0, len(start_videos[j])):
            video_ids = []
            video_titles = []
            mod_sequence = []
            page_infos = []
            r = requests.get('https://www.googleapis.com/youtube/v3/videos?fields=items(id,snippet(title))&part=snippet&id=' + start_videos[j][l] + '&key=' + apiKey)
            data = json.loads(r.text)
            video_ids.append(data['items'][0]['id'])
            video_titles.append(data['items'][0]['snippet']['title'])
            for x in range(0, (len(sequence[j]))):
                #gathering data
                current_data = []
                if (sequence == 'random'):
                    gather_to = 1000
                else:
                    gather_to = sequence[j][x] + 20

                page_token = ''
                total_items = 0
                while (gather_to > 0):
                    #if video_ids[x] in prev_suggestions:
                        #data = prev_suggestions[video_ids[x]]
                    #else:
                    data = get_data(video_ids[x], 50, page_token)
                        #prev_suggestions[video_ids[x]] = data
                    current_data.append(data)
                    try:
                        items = len(data['items'])
                    except:
                        items = 0
                    gather_to = gather_to - items
                    total_items += items
                    if (items == 0):
                        break
                    try:
                        page_token = data['nextPageToken']
                    except:
                        break
                page_infos.append(data['pageInfo']['totalResults'])
                data = []
                for n in range(0, len(current_data)):
                    for m in range(0, 50):
                        try:
                            data.append(current_data[n]['items'][m])
                        except:
                            break

                #choosing correct related video
                #if sequence is set to choose random each time
                if (sequence[j] == 'random'):
                    random_int = random.randint(0,total_items)
                    temp_data = data[random_int]
                    mod_sequence.append( (random_int + 1) )
                    video_ids.append(temp_data['id']['videoId'])
                    video_titles.append(temp_data['snippet']['title'])
                #if sequence[j][x] <= total_items
                elif (sequence[j][x] <= total_items):
                    temp_data = data[(sequence[j][x]-1)]
                    mod_sequence.append(sequence[j][x])
                    video_ids.append(temp_data['id']['videoId'])
                    video_titles.append(temp_data['snippet']['title'])
                #else if sequence[j][x] > total_items
                elif (sequence[j][x] > total_items):
                    if (over_max[j] == 0):
                        temp_data = data[-1]
                        mod_sequence.append(total_items)
                        video_ids.append(temp_data['id']['videoId'])
                        video_titles.append(temp_data['snippet']['title'])
                    if (over_max[j] == 1):
                        needed = sequence[j][x]
                        passes = 0
                        while (needed > total_items):
                            needed = needed - total_items
                            passes += 1
                        temp_data = data[(needed-1)]
                        mod_sequence.append(str(sequence[j][x]) + "(" + str(passes) + "p)")
                        video_ids.append(temp_data['id']['videoId'])
                        video_titles.append(temp_data['snippet']['title'])
                    if (over_max[j] == 2):
                        random_int = random.randint(0,total_items)
                        temp_data = data[random_int]
                        mod_sequence.append( (random_int + 1) )
                        video_ids.append(temp_data['id']['videoId'])
                        video_titles.append(temp_data['snippet']['title'])
                    if (over_max[j] == 3):
                        break

            video_path = "Video progression: "
            for x in range(0, len(video_titles)):
                video_path += str(video_titles[x])
                if (x != (len(video_titles)-1)):
                    video_path += " ---> \n"

            print("\n\n\n\nOriginal Sequence: " + str(orig_sequence))
            print("Modified Sequence: " + str(mod_sequence) + "\n")
            try:
                print( (video_path).translate(non_bmp_map) )
            except:
                uprint(video_path)

            all_data = []
            ids_strs = []
            if (len(video_ids) <= 50):
                ids_strs.append("")
                for x in range(0,len(video_ids)):
                    ids_strs[0] += video_ids[x]
                    if (x != (len(video_ids)-1)):
                         ids_strs[0] += ","
            else:
                for m in range(0, math.ceil(len(video_ids)/50)):
                    ids_strs.append("")
                    for n in range(0,50):
                        try:
                            ids_strs[m] += video_ids[(n+(50*m))]
                            if (m != (math.ceil(len(video_ids)/50)-1)):
                                if (n != 49):
                                    ids_strs[m] += ","
                        except:
                            break

            for x in range(0,len(ids_strs)):
                all_data.append(get_all_data(ids_strs[x]))
            new_data = []
            for n in range(0, len(all_data)):
                for m in range(0, len(all_data[n]['items'])):
                    new_data.append(all_data[n]['items'][m])

            file = ""
            try:
                with open('data.csv', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                    for row in reader:
                        file = row[0].split(",")
                        break
            except:
                file = ""

            if 'degree' not in file:
                with open('data.csv', 'w', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['degree', 'startSequence', 'endSequence', 'id', 'publishedAt', 'sinceEpoch', 'title', 'description', 'channelTitle', 'tags', 'categoryId', 'liveBroadcastContent',
                                 'duration', 'dimension', 'definition', 'caption', 'licensedContent', 'projection', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount',
                                 'commentCount', 'topicCategories', 'titleLength', 'descriptionLength', 'channelTitleLength', 'tagsLength', 'categoryName', 'sequenceNumber',
                                 'over_max', 'totalResults'])
                    writer.writerow([set_names[j], "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
                    for x in range(0, len(new_data)):
                        data = new_data[x]
                        csv_data = get_csv_data(data, x, j)
                        try:
                            page_info = page_infos[x]
                        except:
                            page_info = 'unknown'
                        writer.writerow([csv_data[0], csv_data[1], csv_data[2], csv_data[3], csv_data[4], csv_data[5], csv_data[6], csv_data[7], csv_data[8], csv_data[9],
                                         csv_data[10], csv_data[11], csv_data[12], csv_data[13], csv_data[14], csv_data[15], csv_data[16], csv_data[17], csv_data[18], csv_data[19],
                                         csv_data[20], csv_data[21], csv_data[22], csv_data[23], csv_data[24], csv_data[25], csv_data[26], csv_data[27], csv_data[28], csv_data[29],
                                         csv_data[30], page_info])
            else:
                with open('data.csv', 'a', encoding='utf-8') as f:
                     writer = csv.writer(f)
                     writer.writerow([set_names[j], "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
                     for x in range(0, len(new_data)):
                        data = new_data[x]
                        csv_data = get_csv_data(data, x, j)
                        try:
                            page_info = page_infos[x]
                        except:
                            page_info = 'unknown'
                        writer.writerow([csv_data[0], csv_data[1], csv_data[2], csv_data[3], csv_data[4], csv_data[5], csv_data[6], csv_data[7], csv_data[8], csv_data[9],
                                         csv_data[10], csv_data[11], csv_data[12], csv_data[13], csv_data[14], csv_data[15], csv_data[16], csv_data[17], csv_data[18], csv_data[19],
                                         csv_data[20], csv_data[21], csv_data[22], csv_data[23], csv_data[24], csv_data[25], csv_data[26], csv_data[27], csv_data[28], csv_data[29],
                                         page_info])
