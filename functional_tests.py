from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#爱丽丝听说有一个很酷的在线代办事项应用
		#她去了这个应用的首页
		self.browser.get('http://localhost:8000')

		#她注意到网页的标题和头部都包含了“TO—Do”这个词
		self.assertIn('To-Do',  self.browser.title)
		self.fail('Finish the test!')

#应用邀请她输入一个待办事项

#她在一个文本框里输入了“Buy peacock feathers”
#爱丽丝的爱好是使用家蝇做饵钓鱼

#她按下回车键，页面更新了
#待办事项表格里显示了“1：Buy peacock feathers”

#页面中又显示了一个文本框，可以输入其他的待办事项
#她输入了“Use peacock feathers to make a fly”
#爱丽丝做事很有条理

#页面再次更新，她的清单中显示了这两个待办事项

#爱丽丝想知道这个网址是否会记住她的清单
#她看到网址为她生成了一个唯一的URL
#而且页面中有一下文字解说这个功能

#她访问那个URL，发现她的待办事项列表还在

#她很满意，去睡觉了

if __name__ == '__main__':
	unittest.main(warnings='ignore')

