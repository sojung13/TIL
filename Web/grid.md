## WEB

๐https://flukeout.github.io/ = CSS ๋ด ์ ํ์ ์์ ๊ณต๋ถํ๊ธฐ ์ข์ ๊ฒ์

โคhttps://flexboxfroggy.com/#ko = CSS๋ด flex ๊ณต๋ถํ๊ธฐ ์ข์ ๊ฒ์

์ ๋ ์ฌ์ดํธ ์ฐธ์กฐํ๊ธฐ ๋งค์ฐ ์ข์!!!!!!!!!!!!



### float

- none: ๊ธฐ๋ณธ๊ฐ
- left : ์์๋ฅผ ์ผ์ชฝ์ผ๋ก ๋์
- right : ์์๋ฅผ ์ค๋ฅธ์ชฝ์ผ๋ก ๋์



> clearing float

Float๋ Normal Flow์์ ๋ฒ์ด๋ ๋ถ๋ ์ํ(๋  ์์)

๋ฐ๋ผ์, ์ดํ ์์์ ๋ํ์ฌ Float ์์ฑ์ด ์ ์ฉ๋์ง ์๋๋ก Clearing์ด ํ์์ ์

- ::after : ์ ํํ ์์์ ๋งจ ๋ง์ง๋ง ์์์ผ๋ก ๊ฐ์ ์์๋ฅผ ํ๋ ์์ฑ
  - ๋ณดํต content ์์ฑ๊ณผ ํจ๊ป ์ง์ง์ด, ์์์ ์ฅ์์ฉ ์ฝํ์ธ ๋ฅผ ์ถ๊ฐํ  ๋ ์ฌ์ฉ
- clear ์์ฑ ๋ถ์ฌ

![image-20220207202237713](grid.assets/image-20220207202237713.png)



> Flexbox ๊ตฌ์ฑ ์์

- Flex Container(๋ถ๋ชจ ์์)
  - flexbox ๋ ์ด์์์ ํ์ฑํ๋ ๊ฐ์ฅ ๊ธฐ๋ณธ์ ์ธ ๋ชจ๋ธ
  - Flex Item๋ค์ด ๋์ฌ์๋ ์์ญ
  - display ์์ฑ์ flex ํน์ inline-flex๋ก ์ง์ 
- Flex Item(์์ ์์)
  - ์ปจํ์ด๋์ ์ํด ์๋ ์ปจํ์ธ (๋ฐ์ค)

![image-20220207202721634](grid.assets/image-20220207202721634.png)



> Flex ์์ฑ

- ๋ฐฐ์น ์ค์ 
  - flex-direction
  - flex-wrap
- ๊ณต๊ฐ ๋๋๊ธฐ
  - justify-content(main axis)
  - align-content(cross axis)
- ์ ๋ ฌ
  - align-items(๋ชจ๋  ์์ดํ์ cross axis ๊ธฐ์ค์ผ๋ก)
  - align-self(๊ฐ๋ณ ์์ดํ)



> flex-direction

Main-axis ๊ธฐ์ค ๋ฐฉํฅ ์ค์ 

![image-20220207202908693](grid.assets/image-20220207202908693.png)

> flex-wrap

์์ดํ์ด ์ปจํ์ด๋๋ฅผ ๋ฒ์ด๋๋ ๊ฒฝ์ฐ ํด๋น ์์ญ ๋ด์ ๋ฐฐ์น๋๋๋ก ์ค์ 

์ฆ, ๊ธฐ๋ณธ์ ์ผ๋ก ์ปจํ์ด๋ ์์ญ์ ๋ฒ์ด๋์ง ์๋๋ก ํจ

![image-20220207202953006](grid.assets/image-20220207202953006.png)

- nowrap(๊ธฐ๋ณธ๊ฐ) : ํ ์ค์ ๋ฐฐ์น
- wrap : ๋์น๋ฉด ๊ทธ ๋ค์ ์ค๋ก ๋ฐฐ์น



> justify-content

Main axis๋ฅผ ๊ธฐ์ค์ผ๋ก ๊ณต๊ฐ ๋ฐฐ๋ถ

![image-20220207203037025](grid.assets/image-20220207203037025.png)



> align-content

Cross axis๋ฅผ ๊ธฐ์ค์ผ๋ก ๊ณต๊ฐ ๋ฐฐ๋ถ(์์ดํ์ด ํ ์ค๋ก ๋ฐฐ์น๋๋ ๊ฒฝ์ฐ ํ์ธํ  ์ ์์)

![image-20220207203114740](grid.assets/image-20220207203114740.png)



> align-items

๋ชจ๋  ์์ดํ์ Cross axis๋ฅผ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌ

![image-20220207203155417](grid.assets/image-20220207203155417.png)



> align-self

๊ฐ๋ณ ์์ดํ์ Cross axis ๊ธฐ์ค์ผ๋ก ์ ๋ ฌ

๐ฅ ์ฃผ์ ! ํด๋น ์์ฑ์ ์ปจํ์ด๋์ ์ ์ฉํ๋ ๊ฒ์ด ์๋๋ผ ๊ฐ๋ณ ์์ดํ์ ์ ์ฉ

![image-20220207203252739](grid.assets/image-20220207203252739.png)



> ๊ธฐํ ์์ฑ

- flex-grow : ๋จ์ ์์ญ์ ์์ดํ์ ๋ถ๋ฐฐ. ์๋ ฅ๋ ๊ฐ๋งํผ์ ์์ญ์ ์ฐจ์ง
- order : ๋ฐฐ์น ์์



> ๊ทธ๋ฆฌ๋

https://getbootstrap.com/docs/5.1/layout/grid/

์ ์ฌ์ดํธ๋ฅผ ๋ณด๋ฉด ๊ทธ๋ฆฌ๋ ์ฐธ์กฐํ๊ธฐ ๋งค์ฐ ์ข๋ค!!!!!

![image-20220208211238731](grid.assets/image-20220208211238731.png)

 col-(xs)/ sm/ md/ lg/ xl/ xxl ๋ ๋ทฐ ์ฌ์ด์ฆ์ ๋ง์ถฐ column์ด ๋ฐ์ํ๊ณ ,

๋ค์ ์ซ์๋ 12๋ถํ  ์ค ์ด๋๋งํผ์ ์์ญ์ ์ฐจ์งํ๋๋ ๊ฒ์ด๋ค.