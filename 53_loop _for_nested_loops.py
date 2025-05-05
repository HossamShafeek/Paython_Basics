# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}


for name in peoples:
    print(f'Name: {name}')
    #print(f'Skills and progress for {name} is: {peoples[name]}')
    for skill in peoples[name]:
        print(f'Skill is {peoples[name][skill]}')
