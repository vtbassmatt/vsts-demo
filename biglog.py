import math
import os

jolly_roger = """
                             ud$$$**$$$$$$$bc.                          
                          u@**"        4$$$$$$$Nu                       
                        J                ""#$$$$$$r                     
                       @                       $$$$b                    
                     .F                        ^*3$$$                   
                    :% 4                         J$$$N                  
                    $  :F                       :$$$$$                  
                   4F  9                       J$$$$$$$                 
                   4$   k             4$$$$bed$$$$$$$$$                 
                   $$r  'F            $$$$$$$$$$$$$$$$$r                
                   $$$   b.           $$$$$$$$$$$$$$$$$N                
                   $$$$$k 3eeed$$b    $$$Euec."$$$$$$$$$                
    .@$**N.        $$$$$" $$$$$$F'L $$$$$$$$$$$  $$$$$$$                
    :$$L  'L       $$$$$ 4$$$$$$  * $$$$$$$$$$F  $$$$$$F         edNc   
   @$$$$N  ^k      $$$$$  3$$$$*%   $F4$$$$$$$   $$$$$"        d"  z$N  
   $$$$$$   ^k     '$$$"   #$$$F   .$  $$$$$c.u@$$$          J"  @$$$$r 
   $$$$$$$b   *u    ^$L            $$  $$$$$$$$$$$$u@       $$  d$$$$$$ 
    ^$$$$$$.    "NL   "N. z@*     $$$  $$$$$$$$$$$$$P      $P  d$$$$$$$ 
       ^"*$$$$b   '*L   9$E      4$$$  d$$$$$$$$$$$"     d*   J$$$$$r   
            ^$$$$u  '$.  $$$L     "#" d$$$$$$".@$$    .@$"  z$$$$*"     
              ^$$$$. ^$N.3$$$       4u$$$$$$$ 4$$$  u$*" z$$$"          
                '*$$$$$$$$ *$b      J$$$$$$$b u$$P $"  d$$P             
                   #$$$$$$ 4$ 3*$"$*$ $"$'c@@$$$$ .u@$$$P               
                     "$$$$  ""F~$ $uNr$$$^&J$$$$F $$$$#                 
                       "$$    "$$$bd$.$W$$$$$$$$F $$"                   
                         ?k         ?$$$$$$$$$$$F'*                     
                          9$$bL     z$$$$$$$$$$$F                       
                           $$$$    $$$$$$$$$$$$$                        
                            '#$$c  '$$$$$$$$$"                          
                             .@"#$$$$$$$$$$$$b                          
                           z*      $$$$$$$$$$$$N.                       
                         e"      z$$"  #$$$k  '*$$.                     
                     .u*      u@$P"      '#$$c   "$$c                   
              u@$*\"""       d$$"            "$$$u  ^*$$b.               
            :$F           J$P"                ^$$$c   '"$$$$$$bL        
           d$$  ..      @$#                      #$$b         '#$       
           9$$$$$$b   4$$                          ^$$k         '$      
            "$$6""$b u$$                             '$    d$$$$$P      
              '$F $$$$$"                              ^b  ^$$$$b$       
               '$W$$$$"                                'b@$$$$"         
                                                        ^$$$*  Gilo95'   
                                                        
art from http://www.chris.com/ascii/index.php?art=logos%20and%20insignias/jolly%20roger
"""

min_line_length = os.environ.get("MIN_LINE_LENGTH", 1)
min_line_count = os.environ.get("MIN_LINE_COUNT", 1)

line = jolly_roger * max(1, math.ceil(min_line_length / len(jolly_roger)))
for x in max(1, range(min_line_count)):
  print(f"##vso[task.logissue type=error;]{line}")

print("##vso[task.complete result=Succeeded;]DONE")
