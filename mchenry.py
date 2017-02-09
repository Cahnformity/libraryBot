# Objective: To get a study room whenever I want it.
# Ben Cahn: 2-7-17
# Getting room information ( id number, availability )
import requests
import json
import re
from dateutil.parser import parse
#my_params = {"m": "calscroll", "gid": "445", "date": "2017-02-13"}
# my_data = {"valueA": "keyA": "valueB": "keyB"}
#my_headers = {"Referer": "http://calendar.library.ucsc.edu/booking/mch3",}
#my_url = "http://calendar.library.ucsc.edu/process_roombookings.php"
#response = requests.post(my_url, params=my_params, headers=my_headers).text
#print (response)

#input date as string, any format
#return day of the week
def get_weekday(date):
    weekday = parse(date).weekday()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return days[weekday]

#input date and floor
#returns the cryptic html blob with the id numbers
def get_html(_date, _floor):
    my_url = "http://calendar.library.ucsc.edu/process_roombookings.php"
    my_headers = {"Referer": "http://calendar.library.ucsc.edu/booking/mch3",}
    my_params = {"m": "calscroll", "gid": _floor, "date": _date}
    return requests.post(my_url, params=my_params, headers=my_headers).text

#input time of desired room, and cryptic html response
#returns sid of that room ang time slot
def get_sid(room, time, html):
    lucas_Math = '[0-9]+(?:" onclick="return showBookingForm\(this\.id,\'MCH%s \(7\)\'?)[-\sa-zA-Z:\',]+(%s)' % (room, time)
    return re.search(lucas_Math, html).group(0).split('"')[0]

def book_room(sid, gid, fname, lname, email, nick, q1, q2):
    my_day={
        "sid": sid,
        "gid": gid,
        "fname": fname,
        "lname": lname,
        "email": email,
        "nick": nick,
        "q1": q1,
        "q2": q2,
        "tc": "done",
        "qcount": "2",
        "fid": "108",
    }
    my_url = "http://calendar.library.ucsc.edu/process_roombookings.php"
    cookies = {
        'SS_MID': '20de4f91-8fe5-4090-96bf-516cad01fc8aiuuc459w',
        'III_EXPT_FILE': 'aa4712',
        'III_SESSION_ID': '30197b3df689be92814caab6f37e4f4a',
        'SESSION_LANGUAGE': 'eng',
        '_ga': 'GA1.2.1068664769.1461096932',
        'lc_rbv': 'a%3A1%3A%7Bs%3A44%3A%22XgUHld%2FQ8a79ioW5IKe%2F8C%2FTGJ3UD8%2FoXPchDn2mskc%3D%22%3Bs%3A128%3A%22gcLm3v3l1tZ8vwNi%2Fi7NFsIIqbloTZLDjdXLAYdit4SAx9XsAw%2BHAq5tiOJv8XsreamXm4AgUZ7HVS67gEZSUY31ycpwTDHtl4vYj3pl076gUsnXYZkUOD9qGk%2BhKB5x%22%3B%7D',
        'AWSALB': '39WvSRAFdVuPP1Bfbj+UFkJvf5NzFHqeAnpzprn+Bo7MB5+3Jd1cz9nGELEUMAYDefWi+GJvJcqm3lixEDo28EirqdXZDOCwmFuAcp8NeRC58m3iPxl5+UU/AJxZ',
    }
    headers = {
        'Origin': 'http://calendar.library.ucsc.edu',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://calendar.library.ucsc.edu/booking/mch3',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Content-Length': '0',
    }
    cookies = {
        'SS_MID': '20de4f91-8fe5-4090-96bf-516cad01fc8aiuuc459w',
        'III_EXPT_FILE': 'aa4712',
        'III_SESSION_ID': '30197b3df689be92814caab6f37e4f4a',
        'SESSION_LANGUAGE': 'eng',
        '_ga': 'GA1.2.1068664769.1461096932',
        'lc_rbv': 'a%3A1%3A%7Bs%3A44%3A%22XgUHld%2FQ8a79ioW5IKe%2F8C%2FTGJ3UD8%2FoXPchDn2mskc%3D%22%3Bs%3A128%3A%22gcLm3v3l1tZ8vwNi%2Fi7NFsIIqbloTZLDjdXLAYdit4SAx9XsAw%2BHAq5tiOJv8XsreamXm4AgUZ7HVS67gEZSUY31ycpwTDHtl4vYj3pl076gUsnXYZkUOD9qGk%2BhKB5x%22%3B%7D',
        'AWSALB': '39WvSRAFdVuPP1Bfbj+UFkJvf5NzFHqeAnpzprn+Bo7MB5+3Jd1cz9nGELEUMAYDefWi+GJvJcqm3lixEDo28EirqdXZDOCwmFuAcp8NeRC58m3iPxl5+UU/AJxZ',
    }
    my_params = {"m": "booking_full"}
    return requests.post(my_url, params=my_params, headers=headers, data=my_day, cookies=cookies).text


# Booking the room
# print (get_sid(room=my_room, time=time, html=get_html(date, floor) ) )
