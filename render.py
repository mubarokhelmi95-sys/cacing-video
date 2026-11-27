import asyncio,sys,os,time
from playwright.async_api import async_playwright
# usage: python render.py START END OUTDIR   (frame index, 15 fps, 720x1280)
a,b,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
os.makedirs(out,exist_ok=True)
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg=await br.new_page(viewport={"width":720,"height":1280})
        pg.on("pageerror",lambda e:print("PAGEERR:",str(e)[:1500],flush=True))
        await pg.goto("file://"+os.path.abspath("index.html")); await pg.evaluate("window.ready")
        for f in range(a,b):
            fn=f"{out}/f{f:05d}.jpg"
            if os.path.exists(fn): continue
            t0=time.time()
            await pg.evaluate(f"(()=>{{window.renderFrame({f});window.setOverlay({f}/15)}})()")
            await pg.screenshot(path=fn,type="jpeg",quality=93)
            print(f,round(time.time()-t0,1),flush=True)
        await br.close()
asyncio.run(main())
