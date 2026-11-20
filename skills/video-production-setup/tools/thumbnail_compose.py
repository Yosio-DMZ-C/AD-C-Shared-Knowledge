#!/usr/bin/env python3
"""AD&C 2A thumbnail compositor: faithful PNG overlays and exact Japanese typography.
The AI-generated background is provided separately; this program does not call image AI.
"""
import argparse, hashlib, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
W,H=1280,720
FONT_PATHS=['/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc','/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc']
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def resize_keep(im, rect):
    a,b,c,d=rect; r=min((c-a)/im.width,(d-b)/im.height)
    obj=im.resize((round(im.width*r),round(im.height*r)), Image.Resampling.LANCZOS)
    return obj,(round(a+(c-a-obj.width)/2),round(d-obj.height))
def copy_font(draw, lines, width, high, low, sw, path):
    for pt in range(high,low-1,-1):
        ft=ImageFont.truetype(path,pt,index=0)
        if all(draw.textbbox((0,0),v,font=ft,stroke_width=sw)[2]<=width for v in lines): return ft,pt
    raise ValueError('TEXT_SAFE_AREA_FAIL: change line breaks, never rewrite approved text')
def run(spec_file, background_file, output_dir):
    cfg=json.loads(Path(spec_file).read_text(encoding='utf-8'))
    for k in ('headline','subtitle','headline_lines','subtitle_lines','assets'):
        if k not in cfg: raise ValueError('Missing '+k)
    for k in ('headline','subtitle'):
        if ''.join(cfg[k+'_lines'])!=cfg[k]: raise ValueError('COPY_MISMATCH: '+k)
    for k in ('host','mascot','logo'):
        if k not in cfg['assets']: raise ValueError('Missing official asset '+k)
    fpath=next((p for p in FONT_PATHS if Path(p).is_file()),None)
    if fpath is None: raise RuntimeError('Noto CJK Bold not installed')
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    canvas=ImageOps.fit(Image.open(background_file).convert('RGB'),(W,H),method=Image.Resampling.LANCZOS).convert('RGBA')
    area=Image.new('RGBA',(W,H),(0,0,0,0))
    ImageDraw.Draw(area).rounded_rectangle((247,105,1032,638),radius=43,fill=(249,253,255,185))
    canvas=Image.alpha_composite(canvas,area.filter(ImageFilter.GaussianBlur(12)))
    typeset=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(typeset)
    head=cfg['headline_lines'];sub=cfg['subtitle_lines']
    ft,main_pt=copy_font(d,head,745,94,57,5,fpath)
    lh=min(115,335//len(head))
    for i,txt in enumerate(head):
        bb=d.textbbox((0,0),txt,font=ft,stroke_width=5);x=round((270+1015-(bb[2]-bb[0]))/2)
        d.text((x,110+i*lh),txt,font=ft,fill='#102B4B',stroke_width=5,stroke_fill='#FFFFFF')
    d.rounded_rectangle((480,456,811,463),radius=3,fill='#F2A822')
    fs,sub_pt=copy_font(d,sub,717,53,35,2,fpath)
    sh=min(73,159//len(sub))
    for i,txt in enumerate(sub):
        bb=d.textbbox((0,0),txt,font=fs,stroke_width=2);x=round((283+1000-(bb[2]-bb[0]))/2)
        d.text((x,476+i*sh),txt,font=fs,fill='#133A60',stroke_width=2,stroke_fill='#FFFFFF')
    canvas=Image.alpha_composite(canvas,typeset)
    originals={}
    for role,rect in [('host',(-35,25,260,737)),('mascot',(1016,255,1310,710))]:
        src=Path(cfg['assets'][role]);originals[role]=sha(src)
        im,pos=resize_keep(Image.open(src).convert('RGBA'),rect)
        canvas.alpha_composite(im,dest=pos)
    src=Path(cfg['assets']['logo']);originals['logo']=sha(src)
    official,pos=resize_keep(Image.open(src).convert('RGBA'),(1066,654,1260,710))
    lower=Image.new('RGBA',(W,H),(0,0,0,0))
    ImageDraw.Draw(lower).rounded_rectangle((1057,643,1271,716),radius=14,fill=(255,255,255,236))
    canvas=Image.alpha_composite(canvas,lower)
    canvas.alpha_composite(official,dest=pos)
    final=out/'thumbnail_1280x720.png';preview=out/'preview_320x180.png'
    canvas.convert('RGB').save(final,optimize=True)
    canvas.convert('RGB').resize((320,180),Image.Resampling.LANCZOS).save(preview,optimize=True)
    report={'status':'MECHANICAL_PASS_VISUAL_PENDING','headline_exact':''.join(head)==cfg['headline'],
        'subtitle_exact':''.join(sub)==cfg['subtitle'],'main_font_px':main_pt,'subtitle_font_px':sub_pt,
        'source_sha_unchanged':all(sha(cfg['assets'][k])==v for k,v in originals.items()),
        'source_sha256':originals,'background_sha256':sha(background_file),'full_sha256':sha(final),
        'full_size':[1280,720],'preview_size':[320,180],
        'creative_quality':'HUMAN_REVIEW_REQUIRED','image_generation':'EXTERNAL_NOT_CALLED_BY_SCRIPT'}
    (out/'qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return report

def prepare_guide(spec_file, output_dir):
    """Create a spatial reference only. No AI generation, no altered official source files."""
    cfg=json.loads(Path(spec_file).read_text(encoding='utf-8'))
    for k in ('host','mascot','logo'):
        if k not in cfg.get('assets',{}): raise ValueError('Missing official asset '+k)
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    base=Image.new('RGBA',(W,H),(223,247,250,255));d=ImageDraw.Draw(base)
    d.rounded_rectangle((247,105,1032,638),radius=43,fill=(250,254,255,255),outline=(37,132,153,255),width=6)
    d.rounded_rectangle((265,123,1016,448),radius=20,outline=(175,207,212,255),width=3)
    d.rounded_rectangle((281,477,1003,631),radius=18,outline=(175,207,212,255),width=3)
    originals={}
    for role,rect in [('host',(-35,25,260,737)),('mascot',(1016,255,1310,710))]:
        src=Path(cfg['assets'][role]);originals[role]=sha(src)
        figure,pos=resize_keep(Image.open(src).convert('RGBA'),rect)
        base.alpha_composite(figure,dest=pos)
    src=Path(cfg['assets']['logo']);originals['logo']=sha(src)
    logo,pos=resize_keep(Image.open(src).convert('RGBA'),(1066,654,1260,710))
    base.alpha_composite(logo,dest=pos)
    path=out/'guide_1280x720.png';base.save(path)
    return {'status':'GUIDE_CREATED','image':str(path),'size':[W,H],
            'source_sha_unchanged':all(sha(cfg['assets'][k])==v for k,v in originals.items())}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--manifest',required=True);p.add_argument('--background');p.add_argument('--outdir',required=True);p.add_argument('--guide-only',action='store_true')
    a=p.parse_args();print(json.dumps(prepare_guide(a.manifest,a.outdir) if a.guide_only else run(a.manifest,a.background or p.error('--background required for composition'),a.outdir),ensure_ascii=False,indent=2))
