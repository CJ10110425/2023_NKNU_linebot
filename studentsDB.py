import pymongo
        ## 下面連結得自行連結 ##
myclient = pymongo.MongoClient("mongodb+srv://christmastime20001225:Chrisli1216@cluster0.hxo9fnv.mongodb.net")
mydb= myclient["Student_DB"]
mycol=mydb["Student_profile"]


        ## 學生的資料形式 ##
def insert_userprofile(student_id,student_gender,student_name,student_class):
   mycol.insert_one({"Student_Id":student_id,"Student_gender":student_gender,"Student_name":student_name,"student_class":student_class})
        ## 學生課程要用集合表示 ##



        ## 從學生的課程找尋學生的姓名 ##
def class_to_name(target_student_class):
    classes=[]
        ## 鎖定想查詢課程 ##
    query = {"student_class": {"$in": [target_student_class]}}
        ## 找尋符合相同資料的人 ##
    results = mycol.find(query)
        ## 接接續將相同課程的學生的 "Student_name" 這組資料由 append接續儲存至results ##
    for result in results:
        classes.append(result["Student_name"] )
    return classes 



        ## 從學生的課程找尋學生的ID ##
def class_to_id(target_student_class):
    IDs=[]
        ##鎖定想查詢課程##
    query = {"student_class": {"$in": [target_student_class]}}
        ##找尋符合相同資料的人##
    results = mycol.find(query)
        ##接接續將相同課程的學生的 "Student_name" 這組資料由 append接續儲存至results ##
    for result in results:
        IDs.append(result["Student_ID"] )
    return IDs 