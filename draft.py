import requests

# url = 'https://pjapi.jd.com/book/sort?source=bookSort'
#
# headers = {
#     # 'cookie': '__jdu=1604837363851909553831; unpl=V2_ZzNtbUcEFxV0ChZQfh1aVmILFlwSUUsQIAkVUHJKDAw1VEdfclRCFnQURlRnGFUUZAAZWEJcQBBFCEdkeRtVB2QGFl5KZ3Mldgh2VUsZWwRiChBbQFBBHHEITlVzHVgHbgESbXJQQxxFOHZUcxxcBmECEl5EZ0IldwlHV34eXAZnCyIWLFYOFXIJQ115H14CZQoWXUpWSxFxCk9WeyleBWcAEW1B; __jdv=122270672|go.dlads.cn|t_338324529_|tuiguang|4be103a5457b4950a794d0b58ba8cfd3|1604846484410; shshshfpa=f584b474-ca92-6e45-64f5-802d530bfffe-1604846484; areaId=21; shshshfpb=tPpAs9i5tpvt%20rG%20czqPNiQ%3D%3D; mt_xid=V2_52007VwMVU1hRUFwdThtVAWcLE1pZXFBTHUkpXlJuBBcBXQhODhtNHEAAYwoaTg0IBQoDGh5bBWQBE1pZWFRcL0oYXwR7AxJOXVpDWhtCG1oOZAoiUm1YYlkbSBpbAGMHEVRtWlZbGg%3D%3D; PCSYCityID=CN_360000_360100_0; ipLoc-djd=21-1827-4101-40925; shshshfp=c7ce8073823cfff875e8a64f2ebdb674; __jdc=122270672; 3AB9D23F7A4B3C9B=KZYJHJSHKU7CKVWMKMUOADFRFGMTFEBEP3ZDI5X3GITQYWCOVFQW6J37Z4H2YPPHTSABF7UXE5YGKBRK2ASMVSBNLY; __jda=122270672.1604837363851909553831.1604837363.1605775567.1605780638.11; __jdb=122270672.1.1604837363851909553831|11.1605780638',
#     'referer': 'https://book.jd.com/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
# }
# response = requests.get(url, headers=headers)
#
# print(response.text)


# url = 'https://list.jd.com/listNew.php'
# url2 = 'https://list.jd.com/list.html?cat=1713%2C3258%2C3297'
#
# data = {
#     'cat': '1713,3258,3297',
#     'page': '11',
#     's': '1',
#     'click': '0'
# }
# headers = {
#     'cookie':'__jdu=1604837363851909553831; unpl=V2_ZzNtbUcEFxV0ChZQfh1aVmILFlwSUUsQIAkVUHJKDAw1VEdfclRCFnQURlRnGFUUZAAZWEJcQBBFCEdkeRtVB2QGFl5KZ3Mldgh2VUsZWwRiChBbQFBBHHEITlVzHVgHbgESbXJQQxxFOHZUcxxcBmECEl5EZ0IldwlHV34eXAZnCyIWLFYOFXIJQ115H14CZQoWXUpWSxFxCk9WeyleBWcAEW1B; __jdv=122270672|go.dlads.cn|t_338324529_|tuiguang|4be103a5457b4950a794d0b58ba8cfd3|1604846484410; shshshfpa=f584b474-ca92-6e45-64f5-802d530bfffe-1604846484; areaId=21; shshshfpb=tPpAs9i5tpvt%20rG%20czqPNiQ%3D%3D; PCSYCityID=CN_360000_360100_0; ipLoc-djd=21-1827-4101-40925; __jdc=122270672; __jda=122270672.1604837363851909553831.1604837363.1605780638.1605782831.12; shshshfp=4fdd16484de83368db4519a4907e640a; mt_xid=V2_52007VwMVU1hRUFwdThtVAWcLE1pZXFBTHUkpXgM3VkIBXQxODUpKGUAANFQbTlVYAFkDQRALBWABFAAJWltSL0oYXwR7AxJOXVBDWhdCHF4OYwAiUG1YYlMWQRlZA2cHEldcX1pTGE0dWAxXAxRWWQ%3D%3D; 3AB9D23F7A4B3C9B=KZYJHJSHKU7CKVWMKMUOADFRFGMTFEBEP3ZDI5X3GITQYWCOVFQW6J37Z4H2YPPHTSABF7UXE5YGKBRK2ASMVSBNLY; shshshsID=83e8d6ea99f7837ebfb486d4d8e3f05d_3_1605786989398; __jdb=122270672.24.1604837363851909553831|12.1605782831',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
# }
# response = requests.get(url, data=data, headers=headers)
# with open('res.html', 'w')as e:
#     e.write(response.text)
# print(response.text)



from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
print(driver.page_source)
driver.close()


