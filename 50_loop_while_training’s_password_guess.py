# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break

    print("Will Not Print")

else:
  
  # If Correct Password
  print("Correct Password")

# If Don't Use Else Printing This Text
# If Loop Is Ended
print('The End')