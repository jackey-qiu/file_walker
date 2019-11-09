import os

tags=["project","year","beamline","dataid","participants"]

class file_navigator(object):
    def __init__(self,root_dir=[],tag_file='', search_conditions={}):
        self.root = root_dir
        self.tag_file = tag_file
        self.location_box = []
        self.search_conditions = search_conditions

    def search_file(self):
        for sub_root in self.root:
            for each in os.listdir(sub_root):
                for f in os.listdir(os.path.join(sub_root,each)):
                    if f==self.tag_file:
                        with open(os.path.join(sub_root,each,self.tag_file)) as ff:
                            lines = ff.readlines()
                            tag_temp, tag_value_temp =[],[]
                            for line in lines:
                                tag, tag_value = line.rstrip().rsplit(":")
                                tag_temp.append(tag)
                                tag_value_temp.append(tag_value)
                            if len(self.search_conditions)!=0:
                                if sum([int(self.search_conditions[tag] in tag_value_temp) for tag in self.search_conditions]) == len(self.search_conditions):
                                    self.location_box.append(os.path.join(sub_root,each))
        return None

    def reset_search_condition(self,search_conditions):
        self.search_conditions = search_conditions
        self.location_box = []

    def reset_root(self,root_dir):
        self.root = root_dir

    def reset_tag(self, tag):
        self.tag_file = tag

