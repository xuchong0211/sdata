import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

day = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"

week = "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg"

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sz.002284",
    week,
    start_date='2017-06-01', end_date='2022-06-10',
    frequency="w", adjustflag="2") #frequency="d"取日k线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("~/002284.w.history_k_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()







export const MALE_ALL_IMAGES = {
                                   general: [
                                                { image: "skinImg", key: "skin" },
                                                { image: "allergyImg", key: "allergy" },
                                                { image: "fluImg", key: "infectious" },
                                            // {image: bloodImg, key: 'blood'},
                                   { image: "metabolismImg", key: "metabolism" },
                               { image: "disorderImg", key: "disorder" },
],
// head: [...HEAD_IMAGES, {image: faceMaleImg, key: 'face'}],
head: [
    { image: "brainImg", key: "brain" },
    { image: "eyeImg", key: "eyes" },
    { image: "noseImg", key: "nose" },
    { image: "mouthImg", key: "mouth" },
    { image: "earImg", key: "ear" },
    { image: "faceFemaleImg", key: "face" },
],
neck: [
    { image: "throatImg", key: "throat" },
    { image: "thyroidImg", key: "thyroid" },
    { image: "lymphImg", key: "lymph" },
],
chest: [
    { image: "heartImg", key: "heart" },
    { image: "lungImg", key: "lung" },
],
// upper_limb: UPPER_IMAGES,
upper_limb: [
    { image: "handImg", key: "hand" },
    { image: "elbowImg", key: "upper_bone_joint" },
    { image: "shoulderImg", key: "shoulder" },
    { image: "armImg", key: "arm" },
],
lower_limb: [
    { image: "footImg", key: "foot" },
    { image: "kneeImg", key: "lower_bone_joint" },
    { image: "thighImg", key: "thigh" },
    { image: "crotchImg", key: "crotch" },
],
abdomen: [
             { image: "abdomenImg", key: "abdomen" },
             { image: "epigastricImg", key: "upper_abdomen" },
             { image: "inferiorImg", key: "lower_abdomen" },
             { image: "navelImg", key: "navel" },
         // {image: liverImg, key: 'liver'},
// {image: stomachImg, key: 'stomach'},
// {image: intestinesImg, key: 'intestines'},
// {image: pancreasImg, key: 'pancreas'},
// {image: kidneysImg, key: 'kidneys'},
// {image: urinaryMaleImg, key: 'urinary'},
   { image: "kidneysUrinaryImg", key: "kidneys_urinary" },
   { image: "anusImg", key: "anus" },
   { image: "appendixImg", key: "appendix" },
   { image: "maleGenitalImg", key: "genital" },
   { image: "crotchImg", key: "crotch" },
],
// urinary: [URINARY_IMAGES[0]],
others: [
        // {image: maleGenitalImg, key: 'genital'},

// {image: menopauseImg, key: 'menopause'},
// {image: allergyImg, key: 'allergies'},
//
// {image: fluImg, key: 'infectious'},
// {image: metabolismImg, key: 'metabolism'},
// {image: skinImg, key: 'skin'},
// {image: cancerImg, key: 'cancer'},

   { image: "prostateImg", key: "prostate" },
],
specific: [
          //////////////2
{ image: "pregnancyMovement", key: "pregnancy" },
{ image: "postpartumImg", key: "postpartum" },
{ image: "menopauseImg", key: "menopause" },
null,
//////////////3
{ image: "allergyImg", key: "allergy" },
{ image: "fluImg", key: "infectious" },
{ image: "skinImg", key: "skin" },
///////////////4
{ image: "metabolismImg", key: "metabolism" },
{ image: "nutritionImg", key: "nutrition" },
null,
///////////////////5

                   /////////////1
{ image: "prostateImg", key: "prostate" },
{ image: "cancerImg", key: "cancer" },
null,
],
};

export const FEMALE_ALL_IMAGES = {
                                     head: [
                                         { image: "brainImg", key: "brain" },
                                         { image: "eyeImg", key: "eyes" },
                                         { image: "noseImg", key: "nose" },
                                         { image: "mouthImg", key: "mouth" },
                                         { image: "earImg", key: "ear" },
                                         { image: "faceFemaleImg", key: "face" },
                                     ],
                                     neck: [
                                         { image: "throatImg", key: "throat" },
                                         { image: "lymphImg", key: "lymph" },
                                         { image: "thyroidImg", key: "thyroid" },
                                     ],
                                     chest: [
                                         { image: "heartImg", key: "heart" },
                                         { image: "lungImg", key: "lung" },
                                         { image: "breastImg", key: "breast" },
                                     ],
                                     upper_limb: [
                                         { image: "handImg", key: "hand" },
                                         { image: "elbowImg", key: "upper_bone_joint" },
                                         { image: "shoulderImg", key: "shoulder" },
                                         { image: "armImg", key: "arm" },
                                     ],
                                     lower_limb: [
                                         { image: "footImg", key: "foot" },
                                         { image: "kneeImg", key: "lower_bone_joint" },
                                         { image: "thighImg", key: "thigh" },
                                         { image: "crotchImg", key: "crotch" },
                                     ],
                                     abdomen: [
                                                  { image: "abdomenImg", key: "abdomen" },
                                                  { image: "epigastricImg", key: "upper_abdomen" },
                                                  { image: "inferiorImg", key: "lower_abdomen" },
                                                  { image: "navelImg", key: "navel" },
                                              // {image: kidneysImg, key: 'kidneys'},
                                 // {image: urinaryFemaleImg, key: 'urinary'},
                                 { image: "kidneysUrinaryImg", key: "kidneys_urinary" },
                                 { image: "anusImg", key: "anus" },
                                 { image: "appendixImg", key: "appendix" },
                                 { image: "femaleGenitalImg", key: "genital" },
],
others: [
            { image: "menopauseImg", key: "menopause" },
        // {image: allergyImg, key: 'allergies'},
//
// {image: fluImg, key: 'infectious'},
// {image: metabolismImg, key: 'metabolism'},
// {image: skinImg, key: 'skin'},
// {image: cancerImg, key: 'cancer'},
],
};

export const PREGNANCY_ALL_IMAGES = {
                                        head: [
                                            { image: "brainImg", key: "brain" },
                                            { image: "eyeImg", key: "eyes" },
                                            { image: "noseImg", key: "nose" },
                                            { image: "mouthImg", key: "mouth" },
                                            { image: "earImg", key: "ear" },
                                            { image: "faceFemaleImg", key: "face" },
                                        ],
                                        neck: [
                                            { image: "throatImg", key: "throat" },
                                            { image: "lymphImg", key: "lymph" },
                                            { image: "thyroidImg", key: "thyroid" },
                                        ],
                                        chest: [
                                            { image: "heartImg", key: "heart" },
                                            { image: "lungImg", key: "lung" },
                                            { image: "breastImg", key: "breast" },
                                        ],
                                        upper_limb: [
                                            { image: "handImg", key: "hand" },
                                            { image: "elbowImg", key: "upper_bone_joint" },
                                            { image: "shoulderImg", key: "shoulder" },
                                            { image: "armImg", key: "arm" },
                                        ],
                                        lower_limb: [
                                            { image: "footImg", key: "foot" },
                                            { image: "kneeImg", key: "lower_bone_joint" },
                                            { image: "thighImg", key: "thigh" },
                                            { image: "crotchImg", key: "crotch" },
                                        ],
                                        abdomen: [
                                                     { image: "abdomenImg", key: "abdomen" },
                                                     { image: "epigastricImg", key: "upper_abdomen" },
                                                     { image: "inferiorImg", key: "lower_abdomen" },
                                                     { image: "navelImg", key: "navel" },
                                                 // {image: kidneysImg, key: 'kidneys'},
                                    // {image: urinaryFemaleImg, key: 'urinary'},
                                    { image: "kidneysUrinaryImg", key: "kidneys_urinary" },
                                    { image: "anusImg", key: "anus" },
                                    { image: "appendixImg", key: "appendix" },
                                    { image: "femaleGenitalImg", key: "genital" },
],
others: [
        // {image: pregnancyMovement, key: 'pregnancy'},
// {image: menopauseImg, key: 'menopause'},
// {image: allergyImg, key: 'allergies'},
// {image: fluImg, key: 'infectious'},
// {image: metabolismImg, key: 'metabolism'},
// {image: skinImg, key: 'skin'},
// {image: cancerImg, key: 'cancer'},

   { image: "pregnancyMovement", key: "pregnancy" },
   { image: "postpartumImg", key: "postpartum" },
],
};

export const PEDIATRIC_ALL_IMAGES = {
    head: [
        { image: "brainImg", key: "brain" },
        { image: "noseImg", key: "nose" },
    ],
    neck: [{ image: "throatImg", key: "throat" }],
    chest: [{ image: "lungImg", key: "lung" }],
    abdomen: [
        { image: "navelImg", key: "navel" },
        { image: "abdomenImg", key: "abdomen" },
        { image: "urinaryFemaleImg", key: "urinary" },

        { image: "crotchImg", key: "crotch" },
    ],
    others: [
        { image: "fluImg", key: "infectious" },
        { image: "nutritionImg", key: "nutrition" },
        { image: "skinImg", key: "skin" },
    ],
};

export const FEMALE_ORGAN_PROTOCOL_V1_MAPPING = {
                                                //head
brain: {
    protocols: [97, 98, 99, 101, 102, 103, 104, 109, 105, 106, 107, 108],
},
eyes: {
    protocols: [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94],
},
nose: {
    protocols: [124, 125, 126, 129, 133, 134, 135, 207],
},
mouth: {
    protocols: [208, 209, 210, 211, 212, 213, 214, 215, 74],
},
ear: {
    protocols: [127, 128, 130, 132],
},
face: {
    protocols: [100, 132],
},
//neck
throat: {
    protocols: [122, 123, 131, 135, 207],
},
lymph: {
    protocols: [25],
},
thyroid: {
    protocols: [16],
},
//chest:
heart: {
           protocols: [5, 6, 7, 8, 9, 30],
       },
       lung: {
    protocols: [13, 26, 15, 20, 136, 137],
},
breast: {
    protocols: [120, 219],
},
//Upper limbs

hand: {
    protocols: [67, 76, 201],
},
upper_bone_joint: {
    protocols: [10, 11, 12, 34, 47, 48],
},

shoulder: {
    protocols: [10, 11, 12],
},

arm: {
    protocols: [10, 11, 12],
},

//lower limbs

foot: {
    protocols: [47, 48, 67, 141],
},
lower_bone_joint: {
    protocols: [10, 11, 12, 47, 48],
},

thigh: {
    protocols: [201],
},
crotch: {
    protocols: [25, 50, 76],
},
//abdomen
abdomen: {
    protocols: [3, 19, 32, 39, 52, 139, 140, 141, 142, 143],
},
upper_abdomen: {
    protocols: [4, 23, 36, 31, 42, 28, 29],
},
lower_abdomen: {
    protocols: [2, 21, 24],
},
navel: {
    protocols: [43],
},
kidneys: {
    protocols: [22, 223, 224],
},
urinary: {
    protocols: [22, 223, 224],
},
kidneys_urinary: {
    protocols: [22, 223, 224],
},
anus: {
    protocols: [45],
},
appendix: {
    protocols: [49],
},
genital: {
    protocols: [121, 58, 77, 78, 80, 205],
},

//others
infectious: {
    protocols: [
        13,
        14,
        18,
        19,
        26,
        27,
        28,
        29,
        51,
        74,
        79,
        81,
        95,
        96,
        110,
        132,
        139,
        140,
        141,
        142,
        143,
        52,
        19,
        135,
        206,
        207,
    ],
},
pregnancy: {
    protocols: [30, 38, 111, 112, 113, 114, 115, 116, 117, 118, 119],
},

postpartum: {
    protocols: [30],
},

menopause: {
    protocols: [216, 12],
},
allergies: {
    protocols: [20, 40, 52, 53, 54, 55, 57, 124],
},
metabolism: {
    protocols: [16, 17, 33, 34, 35, 37, 38, 39, 138],
},

skin: {
    protocols: [
        50,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        121,
        80,
    ],
},
cancer: {
    protocols: [209, 221, 217, 218, 219],
},
};

const PEDIATRIC_PROTOCOL_V1_MAPPING = {
                                      //head
brain: {
    protocols: [108],
},
eyes: {
    protocols: [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94],
},
nose: {
    protocols: [135],
},
//neck
throat: {
    protocols: [135],
},
//chest:
lung: {
          protocols: [13, 26, 15, 20, 136, 137],
      },

      foot: {
    protocols: [47, 48, 67, 141],
},
lower_bone_joint: {
    protocols: [10, 11, 12, 47, 48],
},

hips_thigh: {
    protocols: [201],
},
crotch: {
    protocols: [50, 25],
},
//abdomen
abdomen: {
    protocols: [21, 139, 140, 141, 142, 143],
},
navel: {
    protocols: [43],
},
//other

infectious: {
    protocols: [18],
},
nutrition: {
    protocols: [138, 146],
},
skin: {
    protocols: [144, 145],
},
};
