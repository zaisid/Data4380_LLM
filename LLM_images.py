
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import matplotlib
from matplotlib.patches import Rectangle,Circle,Polygon
import matplotlib.colors as mcolors

from google import genai


colors = list(mcolors.BASE_COLORS)
colors.remove("w")

def generate_coord():
    "Outputs a tuple/coordinate point"
    return (rand_num(),rand_num()) #tuple

def distance_formula(coord1,coord2):
    "Calculate distance given two tuples/coordinate points"
    x1,y1 = coord1
    x2,y2 = coord2
    dist = ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    return dist

def is_triangle(coord1,coord2,coord3):
    "Test if real triangle based on 3 points; Boolean output"
    side1 = distance_formula(coord1,coord2)
    side2 = distance_formula(coord3,coord2)
    side3 = distance_formula(coord1,coord3)
    if not (side1+side2>side3 and side1+side3>side1 and side2+side3>side1):
        return False
    if side1 == 0 or side2 == 0 or side3 == 0:
        return False
    else:
        return True

def rand_small_num(limit=0.5):
    "Keeps random number under certain decimal value; automatically set to 0.5"
    h = rand_num()
    while h > limit:
        h /= 2
    return h

def generate_rectangle(w=0.5,h=0.35):
    "Generates rectangle; width/height can be varied"
    return Rectangle(generate_coord(), 
                width=rand_small_num(w), 
                height=rand_small_num(h),
                angle=rand_num()*10,
                facecolor=rand_color(),
                alpha=0.6
                )

def generate_circle(r=0.3):
    "Generates circle; radius can be varied"
    return Circle(generate_coord(),
           radius=rand_small_num(r),
           facecolor=rand_color(),
           alpha=0.6
           )

def generate_triangle():
    "Generates triangle"
    valid_triangle = False
    while not valid_triangle:
        coord1,coord2,coord3 = generate_coord(),generate_coord(),generate_coord()
        valid_triangle = is_triangle(coord1,coord2,coord3)
    
    return Polygon([coord1,
           coord2,
           coord3],
           color=random.choice(colors),
           alpha=0.6
           )

def rand_count(max=5):
    "Returns random whole number; max can be varied"
    return random.randint(0,max)


def multiple_shapes(ax,max=5,limit1=0.5,limit2=0.35,verbose=False):
    """Automatically generates multiple shapes and adds to given figure; can generate string counting each shape type (automatically set to False)"""
    #rectangles
    counter = rand_count(max)
    rect=counter
    while counter > 0:
        rectangle = generate_rectangle(limit1,limit2)
        ax.add_patch(rectangle)
        counter -= 1
    
    #circles
    counter = rand_count(max)
    circ=counter
    while counter > 0:
        circle = generate_circle(limit2)
        ax.add_patch(circle)
        counter -= 1
    
    #triangles
    counter = rand_count(max)
    tri=counter
    while counter > 0:
        triangle = generate_triangle()
        ax.add_patch(triangle)
        counter -= 1

    if verbose:
        return f"There are {rect} rectangles, {circ} circles, and {tri} triangles in this image."
    else:
        return f"r{rect}_c{circ}_t{tri}"


def generate_image(verb=False,max=5,l1=0.3,l2=0.18,path="/Users/zainabsiddiqui/Downloads/Data_Problems/LLM_Project/Data"):
    """Fully generates image with random assortment of shapes & automatically saves figure; descriptive statement can be generated; shape sizes can be adjusted"""
    fig = plt.figure(figsize=(6,6),
                     #frameon=False
                    )
    ax = fig.add_subplot(1, 1, 1,
                         xlim=(-0.2,1.2),
                         ylim=(-0.2,1.2))
    ax.axis('off')
    description = multiple_shapes(ax,max,limit1=l1,limit2=l2,verbose=verb)

    plt.show()
    if verb:
        print(description)
    
        #plt.show()
    else:
        #return description
        save = input(f"""{description}

Save figure?
""").lower().strip()
        if save == "yes":
            fig_name = description+".png"
            fig.savefig(f"{path}/{fig_name}")



#LLM_Test_API.ipynb functions

def get_response(image_path, show=True,
                 model="gemma-3-27b-it",
                 REQUEST="Identify and count the shapes in this image",):
    image = Image.open(image_path)

    response = client.models.generate_content(
      model=model,
      contents=[image, REQUEST],
      )
    
    print(response.text) # The output often is markdown

    #move image after it's tested
    image_path_sep = image_path.split("/") 
    new_path=""
    for dir in image_path_sep[:-1]:
        new_path += f"/{dir}"

    new_path+=f"/Used/{image_path_sep[-1]}"
    
    os.rename(image_path,new_path)

    if show:
        plt.figure(frameon=False)
        plt.imshow(image)
        plt.axis(False)
        plt.show()
