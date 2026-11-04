from flask import Flask
app = Flask(__name__)
HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TOOLS PRO V3</title>
<script>
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box;font-family:system-ui}body{background:#f1f5ff}
header{background:#fff;padding:15px 4%;display:flex;justify-content:space-between;box-shadow:0 2px 15px #0001;position:sticky;top:0;z-index:99}.logo{font-weight:900;font-size:22px;color:#0a5bff}
.tabs{display:flex;gap:10px;overflow:auto;padding:12px 4%;background:#fff;position:sticky;top:58px}.tabs button{white-space:nowrap;border:0;background:#e8efff;padding:10px 18px;border-radius:25px;font-weight:700}.tabs button.active{background:#0a5bff;color:#fff}
.card{max-width:750px;margin:20px auto;background:#fff;border-radius:16px;padding:22px;box-shadow:0 8px 25px #0001}
h3{color:#0a5bff}input,select,textarea{width:100%;padding:13px;border:2px solid #d6e4ff;border-radius:12px;margin:10px 0;font-size:15px}
.btn{background:#0a5bff;color:#fff;border:0;padding:13px;border-radius:12px;font-weight:800;width:100%;font-size:16px;cursor:pointer}
.result{margin-top:15px;padding:15px;background:#f3f7ff;border-radius:12px;word-break:break-all}img{max-width:100%;border-radius:10px}
.style-row{display:flex;justify-content:space-between;align-items:center;padding:12px;border-bottom:1px solid #e8efff}
.range-label{display:flex;justify-content:space-between;font-weight:700;margin-top:10px}
</style></head><body>
<header><div class="logo">🛠️ TOOLS PRO V3</div><div style="font-size:12px;background:#d1ffdd;padding:5px 10px;border-radius:20px">OCR FIXED</div></header>
<div class="tabs">
<button class="active" onclick="show(0)">Thumbnail</button><button onclick="show(1)">Compressor</button><button onclick="show(2)">QR</button><button onclick="show(3)">OCR PRO</button><button onclick="show(4)">Fancy PRO</button>
</div>

<div class="card tool" id="t0"><h3>1. YouTube Thumbnail</h3><input id="yt" placeholder="YouTube link"><button class="btn" onclick="thumb()">Get HD</button><div id="thumbRes" class="result" style="display:none"></div></div>

<div class="card tool" id="t1" style="display:none"><h3>2. Compressor - With % Option</h3><input type="file" id="imgIn" accept="image/*">
<div class="range-label"><span>Compress Quality:</span><span id="qval">60%</span></div><input type="range" id="qrange" min="10" max="95" value="60" oninput="document.getElementById('qval').innerText=this.value+'%'" style="width:100%">
<select id="sizeMode"><option value="quality">Custom % (from slider)</option><option value="50kb">Auto 50KB (WhatsApp)</option><option value="100kb">Auto 100KB</option><option value="200kb">Auto 200KB</option></select>
<button class="btn" onclick="compress()">Compress Now</button><div id="compRes" class="result" style="display:none"></div></div>

<div class="card tool" id="t2" style="display:none"><h3>3. QR Generator</h3><input id="qrText" placeholder="Text/Link"><button class="btn" onclick="makeQR()">Generate</button><div id="qrRes" class="result" style="display:none"><center><div id="qrcode"></div></center></div></div>

<div class="card tool" id="t3" style="display:none"><h3>4. Image to Text - FIXED</h3>
<p style="font-size:13px;color:#666">Tip: Clear photo, normal font wali image use karo. Stylish logo 100% correct nahi padhega.</p>
<select id="ocrLang"><option value="eng">English (Best Result)</option><option value="urd">Urdu</option><option value="hin">Hindi</option></select>
<input type="file" id="ocrIn" accept="image/*"><button class="btn" onclick="doOCR()">Extract Text</button><div id="ocrRes" class="result" style="display:none"></div></div>

<div class="card tool" id="t4" style="display:none"><h3>5. Fancy Name - VIRAL</h3><input id="fancyIn" placeholder="Muhammad" value="Muhammad"><button class="btn" onclick="fancy()">Generate Viral Styles</button><div id="fancyRes" class="result" style="display:none"></div></div>

<script>
function show(n){for(let i=0;i<5;i++){document.getElementById('t'+i).style.display=i==n?'block':'none'}document.querySelectorAll('.tabs button').forEach((b,i)=>b.className=i==n?'active':'')}
function thumb(){let v=document.getElementById('yt').value.trim();let m=v.match(/(?:v=|be\\/|embed\\/|shorts\\/)([A-Za-z0-9_-]{11})/);if(!m)return alert('Link sahi dalo');let id=m[1];let d=document.getElementById('thumbRes');d.style.display='block';d.innerHTML='<img src="https://img.youtube.com/vi/'+id+'/maxresdefault.jpg"><br><br><a href="https://img.youtube.com/vi/'+id+'/maxresdefault.jpg" target="_blank" class="btn" style="display:block;text-align:center;text-decoration:none">⬇ HD Download</a>';}
function compress(){let f=document.getElementById('imgIn').files[0];if(!f)return alert('Image select karo');let q=parseInt(document.getElementById('qrange').value)/100;let mode=document.getElementById('sizeMode').value;let r=new FileReader();r.onload=e=>{let img=new Image();img.onload=()=>{let c=document.createElement('canvas');let scale=mode=='50kb'?0.4:mode=='100kb'?0.6:mode=='200kb'?0.7:0.8;c.width=img.width*scale;c.height=img.height*scale;c.getContext('2d').drawImage(img,0,0,c.width,c.height);let quality=mode=='50kb'?0.25:mode=='100kb'?0.45:mode=='200kb'?0.6:q;let out=c.toDataURL('image/jpeg',quality);let d=document.getElementById('compRes');d.style.display='block';let kb=Math.round(out.length*0.75/1024);d.innerHTML='<p>✅ Done! Approx Size: '+kb+'KB | Quality: '+(quality*100).toFixed(0)+'%</p><img src="'+out+'"><br><br><a href="'+out+'" download="compressed.jpg" class="btn" style="display:block;text-align:center;text-decoration:none">⬇ Download Compressed Image</a>';};img.src=e.target.result;};r.readAsDataURL(f);}
function makeQR(){let t=document.getElementById('qrText').value.trim();if(!t)return alert('Text likho');let box=document.getElementById('qrRes');box.style.display='block';document.getElementById('qrcode').innerHTML='';new QRCode(document.getElementById('qrcode'),{text:t,width:220,height:220});}
async function doOCR(){
 let f=document.getElementById('ocrIn').files[0];if(!f)return alert('Image select karo');
 let lang=document.getElementById('ocrLang').value;let d=document.getElementById('ocrRes');d.style.display='block';d.innerHTML='⏳ Image ko clear karke padh raha hun... 15 sec...';
 let reader=new FileReader();
 reader.onload=e=>{
  let img=new Image();img.onload=async()=>{
   let canvas=document.createElement('canvas');let ctx=canvas.getContext('2d');
   canvas.width=img.width*2;canvas.height=img.height*2;
   ctx.drawImage(img,0,0,canvas.width,canvas.height);
   let imageData=ctx.getImageData(0,0,canvas.width,canvas.height);
   let data=imageData.data;for(let i=0;i<data.length;i+=4){let avg=(data[i]+data[i+1]+data[i+2])/3;let v=avg>128?255:0;data[i]=data[i+1]=data[i+2]=v;}ctx.putImageData(imageData,0,0);
   let processed=canvas.toDataURL();
   try{let res=await Tesseract.recognize(processed,lang,{logger:m=>{}});let text=res.data.text.trim();if(!text) text='Text clear nahi mila. Saaf English wali photo try karo.';d.innerHTML='<b>Text Found:</b><textarea rows="8">'+text+'</textarea><button class="btn" onclick="navigator.clipboard.writeText(document.querySelector(`#ocrRes textarea`).value);alert(`Copied!`)">Copy All</button>';}catch(e){d.innerHTML='Error: '+e}
  };img.src=e.target.result;
 };reader.readAsDataURL(f);
}
function fancy(){
 let t=document.getElementById('fancyIn').value.trim();if(!t)return alert('Naam likho');let up=t.toUpperCase();
 let s=[
  '꧁༒☬ '+t+' ☬༒꧂','★彡['+t+']彡★','『'+t+'』','◥꧁'+t+'꧂◤','『ᴹᴿ』'+t+'࿐',
  'ᴹᴿ°'+t+'°','ᶠᶠ '+t+'','꧁ঔৣ☬✞'+t+'✞☬ঔৣ꧂','༄ᶦᶰᵈ᭄ '+t+'࿐','𝕄𝖗 '+t+' 𝕲𝖆𝖒𝖊𝖗',
  '𝓜𝓻 '+t,'𝕄𝕣 '+t,'ᴍʀ '+t,'𝙼𝚁 '+t+' ᶠᶠ','𝐌𝐑 '+t,
  '⫷'+t+'⫸','『'+up+'』','『'+t+'』ᴮᴼˢˢ','ᴮᴬᴰʙᴏʏ '+t,'『Tᴇᴀᴍ』'+t,
  '༺'+t+'༻','꧁'+t+'꧂','꧁༺'+t+'༻꧂','◥꧁ད'+t+'ཌ꧂◤','☬'+t+'☬',
  '♛'+t+'♛','♔'+t+'♔','乂'+t+'乂','×͜× '+t+' ×͜×','『'+t+'』乡Villain',
  t+' ☠️','꧁༒•'+t+'•༒꧂','☆'+t+'☆','『'+t+'』•ᴮᴼˢˢ','ᴴᴰ '+t,
  '么 '+t+' 么','꧁•⊹٭'+t+'٭⊹•꧂','░▒▓█ '+t+' █▓▒░','𝕯𝖆𝖗𝖐 '+t,'𝔇𝔢𝔳𝔦𝔩 '+t,
  'Ｍｒ '+t,'Mʀ '+t+' 亗','꧁✬◦°'+t+'°◦✬꧂','☆꧁༒☬'+t+'☬༒꧂☆','ᎷᏒ '+t+' ᶠᶠ'
 ];
 let d=document.getElementById('fancyRes');d.style.display='block';
 d.innerHTML=s.map(x=>'<div class="style-row"><span>'+x+'</span><button onclick="navigator.clipboard.writeText(`'+x+'`);this.innerText=`Copied`">Copy</button></div>').join('');
}
</script></body></html>
"""
@app.route('/')
def home():
    return HTML
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
