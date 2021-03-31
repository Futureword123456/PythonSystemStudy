*匹配0次或多次                                 +匹配一次或多次
eg:a*bc                                       eg:a+bc
  aabcd =aabc                                   aabcd =>aabc
  cbc =>bc                                      cbc =>
  
?匹配0次或者1次                                {N}匹配指定的N次
{M，N}匹配M-N次，最大化优先                     \d匹配数字
                                               eg:\d c123d =>123
\w匹配数字和字母
 eg:\w{3} he666=he6                            \s匹配任何空格字符
                                                eg:a\s{2}a cccca accc =>a a
用^匹配以**开头                                  $匹配以**结尾
eg:^he.
hello world =>hel
hello world =

  


