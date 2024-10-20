import argparse
import os
import sys
from colorama import Fore,Back,Style # type: ignore

class someProject:
    def __init__(self, language: str, path: str, name: str):
        self.language = language
        self.path = path + "/" + name
        self.name = name

    def init_golang(self):
        print("Initializing a new Golang project...")
        print("Initializing path is: ", self.path)
        
        if not os.path.exists(self.path):
            #path/name
            os.makedirs(self.path)
            print(Fore.GREEN + "Info:" + Fore.WHITE + "create folder")
        else:
            print(Fore.RED + "Error: Directory already exists" + Fore.WHITE)
            return 

        print("begin to create files.....")

        print("create main.go file")
        file = open(self.path + "/main.go", "w")
        file.write("package main\n\n")
        file.close()

        print("create README.md file")
        file = open(self.path + "/README.md", "w")
        file.write(f"# {self.name}\n")
        file.close()

        print("create .gitignore file")
        file = open(self.path + "/.gitignore", "w")
        file.close()

        print("create Dockerfile file")
        file = open(self.path + "/Dockerfile", "w")
        file.close()

        print("create Makefile file")
        file = open(self.path + "/Makefile", "w")
        file.close()

    
        print("begin to create folders.....")
        os.makedirs(self.path + "/api/v1")
        create_web = input("Do you want to create the web directory? (y/n[default]):")
        if create_web.lower() == 'y':
            os.makedirs(self.path + "/web")
        os.makedirs(self.path + "/config")
        os.makedirs(self.path + "/routes")
        os.makedirs(self.path + "/models")
        os.makedirs(self.path + "/controllers")
        os.makedirs(self.path + "/services")
        os.makedirs(self.path + "/utils")
        os.makedirs(self.path + "/middleware")
        os.makedirs(self.path + "/pkg")
        os.makedirs(self.path + "/scripts")
        os.makedirs(self.path + "/test")
        os.makedirs(self.path + "/docs")
        os.makedirs(self.path + "/cmd")

        #在目录下执行 go mod init
        os.system(f"cd {self.path} && go mod init {self.name}")

    def main(self):
        if self.language == 'golang':
            self.init_golang()
        else:
            print(f"Unsupported language: {self.language}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new project.")
    parser.add_argument('--language', type=str, default='golang', help='Programming language to use for the project')
    parser.add_argument('--path', type=str, default='./', help='Path to the project directory')
    parser.add_argument('--name', type=str, default='amazing_project', help='Name of the project')
    args = parser.parse_args()
    sp = someProject(args.language, args.path, args.name)
    sp.main()