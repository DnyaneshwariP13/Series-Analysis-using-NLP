
from glob import glob
import pandas as pd

#we can use this for loading data for any series

def load_subtitles_dataset(dataset_path):
    subtitles_paths=glob(dataset_path+'/*.ass')
    scripts=[]
    episode_num=[]


    for path in subtitles_paths:
        #read lines
        with open(path,'r',encoding="utf8") as file:
            lines=file.readlines()
            lines=lines[27:] # metadata is upto 27th line
            #here we are removing first nine commas to get the subtitle and then we are joining list of sentences by comma
            lines=[",".join(line.split(',')[9:]) for line in lines]


        #replacing //n in subtitle format with a space
        lines=[ line.replace('\\N','' ) for line in lines]
        script=" ".join(lines)

        #get episode no
        episode=int(path.split('-')[-1].split('.')[0].strip())

        scripts.append(script)
        episode_num.append(episode)


    #putting everything pandas dataframe
    df=pd.DataFrame.from_dict({"episode":episode_num,"script":scripts})
    return df