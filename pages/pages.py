import io
import pathlib
from PIL import Image
import requests as rqs
import os


def synth(sy,sections):
    file = f'../../Website/academic-kickstart/content/projects/{sy}/_index.md'
    sep = '.'
    jpg = 'jpg'
    other = ['mp4']

    def rep(item):

        path = f'../{item}/'
        f = 10

        repitem = lambda nm,w,h: f"""  <a href="https://raw.githubusercontent.com/akhilsadam/WebFiles/master/{item}/{nm}?raw=true" 
            data-pswp-src="https://raw.githubusercontent.com/akhilsadam/WebFiles/master/{item}/{nm}?raw=true"
            data-pswp-width="{w}" 
            data-pswp-height="{h}"
            target="_blank">
            <img src="https://raw.githubusercontent.com/akhilsadam/WebFiles/master/{item}/{nm}?raw=true" alt="" width="{int(w/f)}" height="{int(w/h)}"/>
        </a>"""
        # 
        url = lambda nm: f"https://raw.githubusercontent.com/akhilsadam/WebFiles/master/{item}/{nm}?raw=true"

        for p in os.listdir(path):
            nms = p.split('.')
            if nms[1] != jpg and nms[1] not in other:
                nm = nms[0]
                print(nm)
                im1 = Image.open(path+p).convert('RGB')
                try: im1.save(path+nm+sep+jpg)
                except:
                    print(f"[ERR]: file {nm} not converted")
                else:
                    os.remove(path+p)

        os.system(f'git add ../{item}/')
        os.system(f'git commit -m "[auto] update [glob] {item}"')

        reptext=[]
        for p in os.listdir(path):
            # print(p)
            ext = p.split('.')[1]
            if ext == jpg:
                try: im = Image.open(io.BytesIO(rqs.get(url(p)).content))
                except:
                    print(f"[WARN]: Image {p} does not exist.")
                else:
                    w,h = im.size
                    reptext.append(repitem(p,w,h))
            elif ext in other:
                w = 1920
                h = 1080
                reptext.append(repitem(p, w, h))

        return reptext

    tx = pathlib.Path(f'{sy}.md').read_text()

    for item in sections:

        tx=tx.replace(f'[replace-{item}]','\n'.join(rep(item)))

        os.system(f'touch {file}')
        with open(file,'w') as f:
            f.write(tx)

synth('art',['art','models'])
synth('archvis',['archvis'])

os.system('git add .')
os.system('git commit -m "[auto] update pages"')
os.system('git push')