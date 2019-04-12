from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from random import *
import os
from PIL import Image

import cv2
from matplotlib import pyplot as plt
import numpy as np

import pytesseract
import sys
from PIL import ImageEnhance

def catch_and_store_list(DPLindex,user,password):
    chrome_path = "chromedriver.exe"#"C:\selenium_driver_chrome\chromedriver.exe"#chromedriver.exe執行檔所存在的路徑
    web = webdriver.Chrome(chrome_path)

    web.get("https://isdna1.yzu.edu.tw/CnStdSel/Index.aspx")
    t0 = time.time()
    timeout = False
    c_p_wrong = False
    while(True):
        if(time.time() - t0 > 60):
            timeout = True
            break
        select = Select(web.find_element_by_xpath('//*[@id="DPL_SelCosType"]'))

        select.select_by_index(DPLindex)

        elem = web.find_element_by_id('Txt_User')
        elem.clear()
        elem.send_keys(user)

        elem = web.find_element_by_id('Txt_Password')
        elem.clear()
        elem.send_keys(password)

        web.save_screenshot('screenshot.png')
        element = web.find_element_by_xpath('//*[@id="Panel2"]/table/tbody/tr[2]/td[1]/table[1]/tbody/tr[2]/td[2]/img')
        left = element.location['x']+2
        right = element.location['x'] + element.size['width']
        top = element.location['y']+1
        bottom = element.location['y'] + element.size['height']-1

        #from PIL import Image
        img = Image.open('screenshot.png')
        img = img.crop((left, top, right, bottom))
        img.save('captua.png', 'png')

        img = cv2.imread('captua.png')
        for i in range (0,bottom-top):
            for j in range (0,right-left):
                if img[i,j,0] == 192 and img[i,j,1] == 192 and img[i,j,2] == 192:
                    img[i,j] = [255,255,255]
        cv2.imwrite('remove192.png',img)
 
        #用tesseract灰階化+二質化，自動識別
        threshold = 140    
        table = []    
        for i in range(256):    
            if i < threshold:    
                table.append(0)    
            else:    
                table.append(1)  

        pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
            #result = pytesseract.image_to_string(Image.open('remove192.png'))
        img = Image.open('remove192.png')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(3.0)#去噪
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(10.0)#去噪
        imgry = img.convert('L')
        imgry.save('gremove192.png')
        out = imgry.point(table,'1')
        out.save('bremove192.png')
        #補洞
        img = cv2.imread('bremove192.png' , 0)
        kernel = np.ones((2 , 2) , np.uint8)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('opening.png',opening)
        #補洞^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        imto = Image.open('opening.png')
        result = pytesseract.image_to_string(imto,config="-psm 7")
        exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
        result = ''.join([x for x in result if x not in exclude_char_list])
        #result = result.replace(" ","")
        #result = result.replace("!","")
        #result = result.replace("@","")
        #result = result.replace("#","")
        #result = result.replace("$","")
        #result = result.replace("%","")
        #result = result.replace("^","")
        #result = result.replace("&","")
        #result = result.replace("*","")
        #result = result.replace("(","")
        #result = result.replace(")","")
        #result = result.replace("_","")
        #result = result.replace("+","")
        #result = result.replace("<","")
        #result = result.replace(">","")
        #result = result.replace("?","")
        #result = result.replace("/","")
        #result = result.replace("\\","")
        #result = result.replace(".","")
        #result = result.replace("-","")
        #result = result.replace(",","")
        #result = result.replace("`","")

        #用tesseract灰階化+二質化，自動識別結束
        elem = web.find_element_by_id('Txt_CheckCode')
        elem.clear()
        elem.send_keys(result)
        time.sleep(randint(1,3))
        elem = web.find_element_by_id('btnOK')
        elem.click()
        alert = web.switch_to_alert()

        if str(alert.text)[0:4] == "1.為保":#判斷登入是否成功
            t0 = time.time()
            alert.accept()
            web.get('https://isdna1.yzu.edu.tw/CnStdSel/SelCurr.aspx?Culture=zh-tw')
            web.switch_to_frame(web.find_element_by_name('LeftCosList'))
            #print("pre Catch")
            #抓取所有課表
            select = Select(web.find_element_by_id('DPL_DeptName'))
            #print("select DeptName")
            DPL_DeptName_list = []
            for op in select.options:
                DPL_DeptName_list.append(op.text)

            select = Select(web.find_element_by_id('DPL_Degree'))
            DPL_Degree_list=[]
            for op in select.options:
                DPL_Degree_list.append(op.text)

            fd = open('DPL_Inf.txt', 'w')
            fd.write(str(DPL_DeptName_list)+'\n')
            fd.write(str(DPL_Degree_list)+'\n')
            fd.close()
            
            #select = Select(web.find_element_by_id('DPL_DeptName'))
            #select2 = Select(web.find_element_by_id('DPL_Degree'))
            select = Select(web.find_element_by_id('DPL_Degree'))
            select.select_by_index(5)

            id_courseName_2Dlist = []
            for i in range(len(DPL_DeptName_list)):
                select = Select(web.find_element_by_id('DPL_DeptName'))
                select.select_by_index(i)
                id_courseName_2Dlist.append([])

                #for j in range(len(DPL_Degree_list)): #分年級、暫時不做不然存太多(2倍)
                #    select = Select(web.find_element_by_id('DPL_Degree'))
                #    select.select_by_index(j)
                #    id_courseName_3Dlist[i].append([])
                    
                table = web.find_element_by_id("CosListTable")
                try:
                    tdinputlist = table.find_elements_by_tag_name('input')
                    tdtextlist = table.find_elements_by_tag_name('td')
                    for a in range(len(tdinputlist)):
                        id_courseName_2Dlist[i].append((str(tdinputlist[a].get_attribute('id')),tdtextlist[a].text))
                except:
                    id_courseName_2Dlist[i].append(("null","null"))

            f = open('courseInf.txt', 'w')
            for item in id_courseName_2Dlist:
                f.write(str(item)+'\n')
            f.close()
                
            #抓取所有課表
            break
        elif str(alert.text)[0] == "帳":
            c_p_wrong = True
            break
        else:
            alert.accept() #把跳出的alert點掉
            continue #繼續試登入
    if c_p_wrong:
        web.quit()
        return [1],[2],[3]
    if timeout:
        web.quit()
        return [],[],[]
    else:
        web.quit()
        return DPL_Degree_list, DPL_DeptName_list, id_courseName_2Dlist

def catchstart(DPLindex,user,password,choosedlist):
    chrome_path = "chromedriver.exe"#"C:\selenium_driver_chrome\chromedriver.exe"#chromedriver.exe執行檔所存在的路徑
    web = webdriver.Chrome(chrome_path)

    web.get("https://isdna1.yzu.edu.tw/CnStdSel/Index.aspx")
    t0 = time.time()
    timeout = False
    while(True):
        if(time.time() - t0 > 60):
            timeout = True
            break
        select = Select(web.find_element_by_xpath('//*[@id="DPL_SelCosType"]'))

        select.select_by_index(DPLindex)

        elem = web.find_element_by_id('Txt_User')
        elem.clear()
        elem.send_keys(user)

        elem = web.find_element_by_id('Txt_Password')
        elem.clear()
        elem.send_keys(password)

        web.save_screenshot('screenshot.png')
        element = web.find_element_by_xpath('//*[@id="Panel2"]/table/tbody/tr[2]/td[1]/table[1]/tbody/tr[2]/td[2]/img')
        left = element.location['x']+2
        right = element.location['x'] + element.size['width']
        top = element.location['y']+1
        bottom = element.location['y'] + element.size['height']-1

        #from PIL import Image
        img = Image.open('screenshot.png')
        img = img.crop((left, top, right, bottom))
        img.save('captua.png', 'png')

        img = cv2.imread('captua.png')
        for i in range (0,bottom-top):
            for j in range (0,right-left):
                if img[i,j,0] == 192 and img[i,j,1] == 192 and img[i,j,2] == 192:
                    img[i,j] = [255,255,255]
        cv2.imwrite('remove192.png',img)
 
        #用tesseract灰階化+二質化，自動識別
        threshold = 140    
        table = []    
        for i in range(256):    
            if i < threshold:    
                table.append(0)
            else:    
                table.append(1)
		
        pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
            #result = pytesseract.image_to_string(Image.open('remove192.png'))
        img = Image.open('remove192.png')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(3.0)#去噪
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(10.0)#去噪
        imgry = img.convert('L')
        imgry.save('gremove192.png')
        out = imgry.point(table,'1')
        out.save('bremove192.png')
        #補洞
        img = cv2.imread('bremove192.png' , 0)
        kernel = np.ones((2 , 2) , np.uint8)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('opening.png',opening)
        #補洞^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        imto = Image.open('opening.png')
        result = pytesseract.image_to_string(imto,config="-psm 7")
        exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
        result = ''.join([x for x in result if x not in exclude_char_list])

        #用tesseract灰階化+二質化，自動識別結束
        elem = web.find_element_by_id('Txt_CheckCode')
        elem.clear()
        elem.send_keys(result)
        time.sleep(randint(1,3))
        elem = web.find_element_by_id('btnOK')
        elem.click()
        alert = web.switch_to_alert()
        if str(alert.text)[0:4] == "1.為保":#判斷登入是否成功
            t0 = time.time()
            alert.accept()
            web.get('https://isdna1.yzu.edu.tw/CnStdSel/SelCurr.aspx?Culture=zh-tw')
            web.switch_to_frame(web.find_element_by_name('LeftCosList'))

            select = Select(web.find_element_by_id('DPL_Degree'))
            select.select_by_index(5)


            while time.time() - t0 < 240:
                for i in range(len(choosedlist)):
                    select = Select(web.find_element_by_id('DPL_DeptName'))
                    select.select_by_index(choosedlist[i][2])
                    
                    elemplusbottom = web.find_element_by_id(choosedlist[i][0])
                    elemplusbottom.click()
                    time.sleep(randint(1,3))
                    try:
                        alert = web.switch_to_alert()
                    except:
                        continue
                    alert.accept()
                    #alert = web.switch_to_alert()
                    if str(alert.text)[0:6] == "此課程修課人數":
                        alert.accept()
                    elif str(alert.text)[0:3] == "加選訊息":
                        alert.accept()
                    elif str(alert.text)[0:3] == "完成加選":
                        alert.accept()
                    elif str(alert.text) == "此課程本學期已選過!(r)":
                        alert.accept()
                    else:
                        alert.accept()
                    time.sleep(randint(1,3))
            web.quit()
            web = webdriver.Chrome(chrome_path)
            web.get("https://isdna1.yzu.edu.tw/CnStdSel/Index.aspx")
        else:
            alert.accept() #把跳出的alert點掉
            continue #繼續試登入
        
def checkcount(DPLindex,user,password):
    chrome_path = "chromedriver.exe"#"C:\selenium_driver_chrome\chromedriver.exe"#chromedriver.exe執行檔所存在的路徑
    web = webdriver.Chrome(chrome_path)

    web.get("https://isdna1.yzu.edu.tw/CnStdSel/Index.aspx")
    t0 = time.time()
    timeout = False
    while(True):
        if(time.time() - t0 > 60):
            timeout = True
            break
        select = Select(web.find_element_by_xpath('//*[@id="DPL_SelCosType"]'))

        select.select_by_index(DPLindex)

        elem = web.find_element_by_id('Txt_User')
        elem.clear()
        elem.send_keys(user)

        elem = web.find_element_by_id('Txt_Password')
        elem.clear()
        elem.send_keys(password)

        web.save_screenshot('screenshot.png')
        element = web.find_element_by_xpath('//*[@id="Panel2"]/table/tbody/tr[2]/td[1]/table[1]/tbody/tr[2]/td[2]/img')
        left = element.location['x']+2
        right = element.location['x'] + element.size['width']
        top = element.location['y']+1
        bottom = element.location['y'] + element.size['height']-1

        #from PIL import Image
        img = Image.open('screenshot.png')
        img = img.crop((left, top, right, bottom))
        img.save('captua.png', 'png')

        img = cv2.imread('captua.png')
        for i in range (0,bottom-top):
            for j in range (0,right-left):
                if img[i,j,0] == 192 and img[i,j,1] == 192 and img[i,j,2] == 192:
                    img[i,j] = [255,255,255]
        cv2.imwrite('remove192.png',img)
 
        #用tesseract灰階化+二質化，自動識別
        threshold = 140    
        table = []    
        for i in range(256):    
            if i < threshold:    
                table.append(0)
            else:    
                table.append(1)
		
        pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
            #result = pytesseract.image_to_string(Image.open('remove192.png'))
        img = Image.open('remove192.png')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(3.0)#去噪
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(10.0)#去噪
        imgry = img.convert('L')
        imgry.save('gremove192.png')
        out = imgry.point(table,'1')
        out.save('bremove192.png')
        #補洞
        img = cv2.imread('bremove192.png' , 0)
        kernel = np.ones((2 , 2) , np.uint8)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('opening.png',opening)
        #補洞^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        imto = Image.open('opening.png')
        result = pytesseract.image_to_string(imto,config="-psm 7")
        exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
        result = ''.join([x for x in result if x not in exclude_char_list])

        #用tesseract灰階化+二質化，自動識別結束
        elem = web.find_element_by_id('Txt_CheckCode')
        elem.clear()
        elem.send_keys(result)
        time.sleep(randint(1,3))
        elem = web.find_element_by_id('btnOK')
        elem.click()
        alert = web.switch_to_alert()
        if str(alert.text)[0:4] == "1.為保":#判斷登入是否成功
            web.quit()
            return True
        elif str(alert.text)[0] == "帳":
            web.quit()
            return False
        else:
            alert.accept() #把跳出的alert點掉
            continue #繼續試登入
