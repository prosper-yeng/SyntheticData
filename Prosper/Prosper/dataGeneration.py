import random
import time
import csv
import pandas as pd

path_folder =""

#role

shift1 = {
  "id": 1,
  "start": "1/1/2019 6:00 AM",
  "end": "1/1/2019 2:00 PM",
  "employees": ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11' 'e12', 'e13', 'e14', 'e15'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift2 = {
  "id": 2,
  "start": "1/1/2019 2:00 PM",
  "end": "1/1/2019 10:00 PM",
  "employees": ['e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29', 'e30'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift3 = {
  "id": 3,
  "start": "1/1/2019 10:00 PM",
  "end": "1/2/2019 6:00 AM",
  "employees": ['e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39', 'e40', 'e41', 'e42', 'e43', 'e44', 'e45'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift4 = {
  "id": 4,
  "start": "1/2/2019 6:00 AM",
  "end": "1/2/2019 2:00 PM",
  "employees": ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11' 'e12', 'e13', 'e14', 'e15'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift5 = {
  "id": 5,
  "start": "1/2/2019 2:00 PM",
  "end": "1/2/2019 10:00 PM",
  "employees": ['e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29', 'e30'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift6 = {
  "id": 6,
  "start": "1/2/2019 10:00 PM",
  "end": "1/3/2019 6:00 AM",
  "employees": ['e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39', 'e40', 'e41', 'e42', 'e43', 'e44', 'e45'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift7 = {
  "id": 7,
  "start": "1/3/2019 6:00 AM",
  "end": "1/3/2019 2:00 PM",
  "employees": ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11' 'e12', 'e13', 'e14', 'e15'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift8 = {
  "id": 8,
  "start": "1/3/2019 2:00 PM",
  "end": "1/3/2019 10:00 PM",
  "employees": ['e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29', 'e30'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

shift9 = {
  "id": 9,
  "start": "1/3/2019 10:00 PM",
  "end": "1/4/2019 6:00 AM",
  "employees": ['e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39', 'e40', 'e41', 'e42', 'e43', 'e44', 'e45'],
  "roles": ['r1', 'r1','r1','r1','r1', 'r2', 'r2', 'r2','r2','r2','r2','r2','r2', 'r3', 'r3'],
  "departments": ['d1', 'd1', 'd2', 'd2','d3', 'd1','d1', 'd1','d1', 'd3', 'd3','d3','d3','d3', 'd1', 'd2']
}

patients = [['p1', 'd1'], ['p2', 'd1'], ['p3', 'd1'], ['p3', 'd1'], ['p3', 'd1'], ['p4', 'd1'], ['p5', 'd1'], ['p6', 'd2'], ['p7', 'd2'], ['p8', 'd2'], ['p9', 'd2'], ['p10', 'd2']]

schedules= [[shift1, shift2, shift3], [shift4, shift5, shift6], [shift7, shift8, shift9]]

prob_accessPatientRecord= 7
default_maxAccessDuration= 900
default_ipPrefix= '192.168.2.'
departmentIPRange = [['d1', 11, 50], ['d2', 51, 90], ['d3', 91, 105]]
organizationID = 'o1'
default_OS = 'os1'
default_browser = 'b1'
default_device = 'd1'

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return ptime


def random_date(start, end, format, prop):
    return str_time_prop(start, end, format, prop)

format = '%m/%d/%Y %I:%M %p'

list_data = []

for s in schedules:
  for shift in s:
    for employee, role, department in zip(shift['employees'], shift['roles'], shift['departments']):
      for patient in patients:
        if(patient[1]==department):
          proba_acees = random.randrange(10)
          if(proba_acees<prob_accessPatientRecord):
            startAccessTime=random_date(shift['start'], shift['end'], format, random.random())
            #set some rules
            diff= random.randint(60, default_maxAccessDuration) #seconds
            
            endAccessTime=startAccessTime+diff
            
            startAccessTime=time.strftime(format, time.localtime(startAccessTime))
            endAccessTime=time.strftime(format, time.localtime(endAccessTime))
            print( 'startAccessTime: '+startAccessTime)
            print( 'endAccessTime: '+endAccessTime)

            employeeID=employee
            print('employeeID: '+str(employeeID))

            patientID=patient[0]
            print('patientID: '+str(patientID))

            activityID=random.randint(1, 10)
            print('activityID: '+str(activityID))

            min_ip = [dep[1] for dep in departmentIPRange if dep[0]==department][0]
            max_ip = [dep[2] for dep in departmentIPRange if dep[0]==department][0]
            ipAddress = default_ipPrefix+str(random.randint(min_ip, max_ip))
            print('ipAddress: '+str(ipAddress))

            employeeDepartmentID=department
            print('employeeDepartmentID: '+str(employeeDepartmentID))

            employeeOrganizationID=organizationID
            print('employeeOrganizationID: '+str(employeeOrganizationID))

            osID=default_OS
            print('osID: '+str(osID))

            deviceID=default_device
            print('deviceID: '+str(deviceID))

            browserID=default_browser
            print('browserID: '+str(browserID))

            ReasonID=0
            print('ReasonID: '+str(ReasonID))

            shiftID=shift['id']
            print('shiftID: '+str(shiftID))

            #sift time 
            siftStartDateTime=shift['start']

            siftEndDateTime=shift['end']
            
            #siftStartDateTime=time.strftime(format, time.localtime(siftStartDateTime))
            #siftEndDateTime=time.strftime(format, time.localtime(siftEndDateTime))
            
            print( 'siftStartDateTime: '+siftEndDateTime)
            print( 'siftEndDateTime: '+siftEndDateTime)


            CRUD=random.randint(1, 10)
            print('CRUD: '+str(CRUD))

            AccessControlStatus=random.randint(1, 10)
            print('AccessControlStatus: '+str(AccessControlStatus))

            SessionID=random.randint(1, 10)
            print('SessionID: '+str(SessionID))

            AccessPatient_Warnings=random.randint(0, 2)
            print('AccessPatient_Warnings: '+str(AccessPatient_Warnings))

            ModuleUsed=random.randint(1, 10)
            print('ModuleUsed: '+str(ModuleUsed))

            data=[startAccessTime, endAccessTime, employeeID, patientID, activityID, ipAddress, employeeDepartmentID, employeeOrganizationID, osID, deviceID, browserID, ReasonID, shiftID, siftStartDateTime, siftEndDateTime, CRUD, AccessControlStatus, SessionID, AccessPatient_Warnings, ModuleUsed]

            print(data)
            list_data.append(data)

df = pd.DataFrame(list_data, columns=['startAccessTime', 'endAccessTime', 'employeeID', 'patientID', 'activityID', 'ipAddress', 'employeeDepartmentID', 'employeeOrganizationID', 'osID', 'deviceID', 'browserID', 'ReasonID', 'shiftID', 'siftStartDateTime', 'siftEndDateTime', 'CRUD', 'AccessControlStatus', 'SessionID', 'AccessPatient_Warnings', 'ModuleUsed'])
with pd.ExcelWriter(path_folder+'data.xlsx') as writer:  
  df.to_excel(writer, sheet_name='data', index=False)