from .....utilities import datetimes

class ParametricDesignData:
    
    def __init__( self, data:dict = {}, **kwargs ):
        self._data = { **data, **kwargs }
    
    def __str__(self):
        fts = self.get_function_types(True, True)
        pts = self.get_plot_types(True, True)
        polys = self.get_plot_polygons(True, True)
        
        display = []
        non_specific = '{ft}: {count} feature(s)'
        specific = '{ft}[{pt}]: {count} feature(s)'
        for i in range(len(pts)):
            line = non_specific if pts[i] == '-1' else specific
            display.append(
                    line.format(
                            ft=fts[i],
                            pt=pts[i],
                            count=len(polys[i])
                        )
                )
        display = ', '.join(display)
        
        return 'ParametricDesignData: {data}'.format(
                data=display
            )
    
    
    def get_detail_key(self, detail:bool = True):
        return 'detailMPs' if detail else 'bandMPs'
        
    def get_detail_set(self, detail:bool = True):
        return self._data.get( self.get_detail_key(detail), [] )
    
    def get_function_types(self, detail:bool = True, include_remainder:bool = False):
        dataset = self.get_detail_set(detail)
        function_types = []
        for function_type in dataset.keys():
            if function_type == 'REMAINDER' and include_remainder == False:
                continue
            plot_types = dataset[function_type].keys()
            function_types =  function_types + [function_type for pt in plot_types]
        return function_types
    
    def get_plot_types(self, detail:bool = True, include_remainder:bool = False):
        dataset = self.get_detail_set(detail)
        plot_types = []
        for key in dataset.keys():
            if key == 'REMAINDER' and include_remainder == False:
                continue
            plot_types = plot_types + list(dataset[key].keys())
        return list( plot_types )  
        
        
    def get_plot_polygons(self, detail:bool = True, include_remainder:bool = False):
        dataset = self.get_detail_set(detail)
        
        fts = self.get_function_types(True, True)
        pts = self.get_plot_types(True, True)
        
        polygons = []
        
        for i in range(len(pts)):
            if fts[i] == 'REMAINDER' and include_remainder == False:
                continue
            plot_polygons = dataset[fts[i]][pts[i]]
            polygons.append(plot_polygons)
        
        return polygons