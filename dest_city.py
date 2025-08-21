class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destCities=set()
        i=0
        end_cities=set()
        if len(paths)==1:
            return paths[0][1]       
        while(i<len(paths)):

        
            cities=len(paths[i])
           
            for j in range(cities):
            
           

            
                if paths[i][j] not in destCities:
                    destCities.add(paths[i][j])
                    if j==1:
                        end_cities.add(paths[i][1])
                    print("the end city is",end_cities)
                
                
                else:
                    destCities.remove(paths[i][j])
            
            i=i+1
        
        for city in destCities:
            if city in end_cities:
                return city
        
      
        
        
