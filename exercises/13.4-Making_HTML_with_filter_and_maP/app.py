all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(filtered_colors):
    filtered_list = list(filter(lambda x: x["sexy"] is True, all_colors))
    
    return filtered_list

def generate_li(colorlist):
    li_list = []
    li_color = []
    for color in colorlist:
        
        li_color= ["<li>" + str(color["label"]) + "</li>"]
        #li_list = li_list + li_color
        li_list += li_color
        
    return li_list

print(generate_li(filter_colors(all_colors)))