# Project 1

## Project Scores

- **Jobby**: [View Details](./Scores/Jobby.csv/)
- **Tracking System**: [View Details](./Scores/Tracking_System.csv/)
- **Git Simplified**: [View Details](./Scores/Git_Simplified.csv/)
- **Slash**: [View Details](./Scores/Slash.csv/)
- **Simplii**: [View Details](./Scores/Simplii.csv/)

**Updating the Evaluation Tables**
To maintain consistent formatting and simplify updates, we use a script (csv_to_markdown.py) that converts our CSV evaluation files into Markdown tables.

**Prerequisites**
Python (3.x recommended)

**Steps to Update the Table:**
- First, ensure you have updated your CSV file with the new data. The CSV file should have the structure Criteria,Score,Comments.

- Run the csv_to_markdown.py script with the path to your CSV file and the path to the markdown file you want to update as arguments.
 Example/ python csv_to_markdown.py path_to_csv_file.csv Projectname.md 

- The script will append the updated table to the specified markdown file.

- Check the markdown file to ensure the table is correctly formatted and placed.

- Commit and push your changes to the repository.

## 🎥Video of Working Project(GITS)

[![IMAGE ALT TEXT](http://img.youtube.com/vi/MBB66yQVwy8/0.jpg)](http://www.youtube.com/watch?v=MBB66yQVwy8 "csc510 working gits")

##Essay 
> ### 🔍 Challenges Faced 🔍

- **Outdated Dependencies**: Some projects relied on specific software dependencies and libraries that had either been deprecated or updated significantly since the code was written. Trying to find the exact versions or suitable substitutes was a demanding task.

- **Lack of Documentation**: A significant pain point was the lack of comprehensive documentation. While there were comments within the code, a broader overview or setup guide was missing, which made understanding the code's flow and dependencies harder. There was even a link to documentation for a particular function in the README that when clicked threw a "404 - page not found" error.

- **Lack of Examples for functions**: For the documentation that was provided for the various functions there were parts that went unexplained. An example of this could be the listing of various optional flags without any explination for the purpose or advantages of using the flags.

- **Code Complexity and Clarity**: Some sections of the code were intricate, with functions spanning multiple lines without clear segmentation or descriptive variable naming. This complexity made deciphering the code's purpose and function challenging. It is unclear if the project currently has any style guide for there code as there is no mention of it. Having an indication of there being a style guide would be helpful for when properly evluating the code. It also seems that there was still some testing going on during the last phase of the project as there are lingering commented print statements that are assumable for testing and debugging.

- **Platform Compatibility Issues**: The Gits project we chose seemed to have been developed for a particular operating system and is currently unable to run on Windows (except for Windows 10 using WSL). Running it on a different platform required tweaks and adjustments, indicating a lack of cross-platform foresight. There is recommendations to alleviate the issue with the project not being able to be ran on your platform but they offer no insight as to why there is this issue. With the project not being able to run on Windows the possibility for open-source colloboration in the future is skewed because some developers, or even users, may not touch this project due to that one limitation.

- **Issues with README**: A glaring issue with the README is that it is mearly a wall of text that seems never-ending. It is not organized the best or optimized for users to quickly access the knowledge about the project that they would want. For example when mentioning the documentation for the various functions of the program there is a wall of text that list every single function rather than pointing the user to the /docs sub-directory where, if the user wants, could find that information. Some of the README can be condensed into specialized sub-directories if the user want to read more about a particular subject pertaining to the project.

> ### **🛠️ Solutions and Learnings** (Avoiding the Pain) 🛠️

To tackle these challenges, we took a systematic approach:

- **Code Inspection**: Before even attempting to run the system we studied the code, especially the README files, for any setup instructions. This helped us understand the overall architecture and identify potential pitfalls.
  
- **Dependencies**: We quickly realized the importance of virtual environments. Different projects might require different versions of libraries, and without virtual environments, managing these would be nightmarish.
  
- **Testing**: After setting up, running tests (if available) gave us a good idea of what's working and what's not. This was our first real interaction with the system.

> ### **🌟 Best Practices for Future 🌟** (Commitments for Project2)

For our subsequent projects, we are committed to:

1. **Documentation**: Writing comprehensive documentation, especially a more organized and detailed README with setup instructions, known issues, and solutions. This will allow users to better understand the tool and all of its functionality without having to spend an unneccessary amount of time that could otherwise be spent using the tool. Another part of building upon the documentation would be defining and explaining a clear set of exmaples of the tool.
   
2. **Version Control**: Clearly mentioning required versions for all dependencies. This will help users setup the tool and get running quickly so they are not stuck trying to install what they think might be the correct version of the dependencies used in the project
   
3. **Testing**: Regularly updating and running tests, ensuring they cover a significant portion of the codebase. This will allow for the users to see that the code is up-to-date and has that all of the information they had previously read such as dependency versions and such are still accurate.

