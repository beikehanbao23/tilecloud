from tilecloud.layout.template import TemplateTileLayout
from tilecloud.store.url import URLTileStore


tilestore = URLTileStore(
    (TemplateTileLayout('http://datahive.minedata.cn/mergeddata/Villtown,Road,Railway,Ptline,Adminflag,Poi,Annotation,Worldannotation/%(z)d/%(x)d/%(y)d?token=449ba822788c46bea9f90dfba48e5269&solu=4024'.format(server)) for server in 'abc'),
    attribution='&copy; Minedata contributors, willmap', content_type='image/pbf')
