def logincheck(uname,pwd):
    if (uname=="admin" and pwd=="admin123"):
        return "login success"
    if (uname!="admin" and pwd=="admin"):
        return "login fail"
    if (uname=="admin" and pwd!="admin123"):
        return "login fail"
    if (uname!="admin" and pwd!="admin123"):
        return "login fail"


import unittest
class loginclass(unittest.TestCase):
     def test1(self):
         result=logincheck("admin","admin123")
         self.assertEqual(result,"success")
     def test2(self):
          result=logincheck("admin2","admin123")
          self.assertEqual(result,"fail")
     def test3(self):
          result=logincheck("admin","1234")
          self.asserEqual(result,"fail")
     def test4(self):
          result=logincheck("admin2","1234")
          self.asserEqual(result,"fail")    
if __name__=='__main__':
     unittest.main()

    
            
