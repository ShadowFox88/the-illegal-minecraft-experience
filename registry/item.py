class Item:
    def __init__(self, item_id, item_name, item_desc, item_tag : dict):
        self.item_id = item_id
        self.item_name = item_name
        self.item_desc = item_desc

        self.item_tag : dict = item_tag

        self.fun = None

    def bind_use(self, use_fun):
        self.fun = use_fun

    def get_oc_fun(self):
        if self.fun:
            return self.fun   

    def check_tag(self):
        return self.item_tag

    def check_tag_section(self, tag_name):
        try:
            return self.item_tag[tag_name]
        except KeyError:
            return "Doesn't exist"

    def json(self):
        return {
            "item_id":self.item_id,
            "item_name":self.item_name,
            "item_desc":self.item_desc,
            "mwtf_tag":self.item_tag,
            "function": self.fun
        }


# are we making the crafting recipe a parameter or will we need to code it seperately.
# item_object.py has a list of items.