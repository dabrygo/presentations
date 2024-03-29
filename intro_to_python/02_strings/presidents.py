# https://www.whitehouse.gov/about-the-white-house/presidents/
names = """\
George Washington
John Adams
Thomas Jefferson
James Madison
James Monroe
John Quincy Adams
Andrew Jackson
Martin Van Buren
William Henry Harrison
John Tyler
James K. Polk
Zachary Taylor
Millard Fillmore
Franklin Pierce
James Buchanan
Abraham Lincoln
Andrew Johnson
Ulysses S. Grant
Rutherford B. Hayes
James Garfield
Chester A. Arthur
Grover Cleveland
Benjamin Harrison
Grover Cleveland
William McKinley
Theodore Roosevelt
William Howard Taft
Woodrow Wilson
Warren G. Harding
Calvin Coolidge
Herbert Hoover
Franklin D. Roosevelt
Harry S. Truman
Dwight D. Eisenhower
John F. Kennedy
Lyndon B. Johnson
Richard M. Nixon
Gerald R. Ford
James Carter
Ronald Reagan
George H. W. Bush
William J. Clinton
George W. Bush
Barack Obama
Donald J. Trump
"""

presidents = names.splitlines()
for index, president in enumerate(presidents, start=1):
    answer = input(f"Who was U.S. President #{index}?\n>>> ")
    if answer.lower() in president.lower():
        print(f"Yup! President #{index} was {president}!")
    else:
        print(f"Nope, president #{index} was {president}.")
    print()
