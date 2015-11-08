require 'watir-webdriver'

When(/^she go to check out its homepage.$/) do
  @b = Watir::Browser.new :firefox
  @b.goto "http://127.0.0.1:8000"
end

Then(/^she notices the page title and header mention to\-do lists$/) do 
  t = @b.title
  @b.close
  raise "ee" unless t.include?"To-Do"	
end

