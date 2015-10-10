# -*- coding: utf-8 -*-

from graph import Graph
import json
import codecs
from graph_search import shortest_path_search, lowest_cost_search

with codecs.open('routes.txt', 'r', 'utf-8') as f:
    SH = json.load(f)

def path_state(path):
    "return a list of states in a path"
    return path[::2]

def goal_fn(goal):
    return lambda x: x == goal

def action_cost(action1, state1, action, state):
    if action1 is not None and action1 != action:
        return 2
    return 1
    
def test():
    assert path_state(shortest_path_search(u'大华三路', goal_fn(u'行知路'), SH)) == [u'大华三路', u'行知路']
    #assert path_state(shortest_path_search(u'大华三路', goal_fn(u''), SH)) == [u'大华三路', u'新村路', u'岚皋路', u'镇坪路', u'中潭路', u'上海火车站']
    #print '\n'.join(path_state(shortest_path_search(u'大华三路', goal_fn(u'安亭'), SH)))
    #print '\n'.join(shortest_path_search(u'大华三路', goal_fn(u'安亭'), SH))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'大华三路', goal_fn(u'东昌路'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'大华三路', goal_fn(u'人民广场'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'镇坪路', goal_fn(u'世纪大道'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'大华三路', goal_fn(u'大世界'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'大华三路', goal_fn(u'滴水湖'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'大华三路', goal_fn(u'南翔'), SH, action_cost)))
    print '--'*40
    print '->'.join(path_state(lowest_cost_search(u'昌平路', goal_fn(u'桃浦新村'), SH, action_cost)))
    ## for e in lowest_cost_search(u'镇坪路', goal_fn(u'世纪大道'), SH, action_cost):
    ##     print e
    ## for e in shortest_path_search(u'镇坪路', goal_fn(u'世纪大道'), SH):
    ##     print e
    ## print 'test passses'
    
if __name__ == '__main__':
    test()

## if __name__ == '__main__':
##     g = Graph(SH, 'all_edges.txt')
##     print "All the stations:"
##     #print '\n'.join(g.vertices())
##     print '-'*50
##     #print '\n'.join([u"从 %s 到 %s " % (v1, v2) for v1, v2 in g.edges()])
##     print 'Writing all edges to a file'
##     #import json
##     #import codecs
##     #f = codecs.open('all_edges.txt', encoding='utf-8', mode='w')u
##     #edges = g.edges()
##     #d = {}
##     #for v1, v2 in edges:
##     #    d[u"%s %s" % (v1, v2)] = {'distance': 1500, 'travel_time': 120}
##     #json.dump(d, f, ensure_ascii=False)
##     #f.close()
##     print 'wrote to file success'
##     print '-'*50
##     print 'print all %s transfer stations:' % len(g.transfer_stations())
##     print '\n'.join(g.transfer_stations())    
##     print '-'*50
##     print u'查询从大华三路到镇坪路'
##     print '\n'.join(['->'.join([o.ljust(8) for o in e]) for e in g.find_all_paths(u'大华三路', u'镇坪路')])
##     print u'查询从镇坪路到上海火车站'
##     #print '\n'.join(['->'.join([o.ljust(8) for o in e]) for e in g.find_all_paths(u'镇坪路', u'中潭路')])
##     print g.find_shortest_path(u'镇坪路', u'中潭路')
##     print u'查询从大华三路到上海火车站'
##     print '\n--------\n'.join(['->'.join([o.ljust(8) for o in e]) for e in g.find_all_paths(u'大华三路', u'上海火车站')])
##     print u'最短路线是:'
## #    print '\n'.join(g.find_path(u'大华三路', u'上海火车站'))
##     print '\n'.join(g.find_shortest_path(u'大华三路', u'上海火车站'))
## #    path = g.find_shortest_path(u'大华三路', u'上海火车站')
##     #print path
##     #print dir(g)
##     #links = g.path_to_links(path)
##     #print links
##     #time = g.calculate_travel_time(path)
## #    print 'Travel time is: %s seconds.' % time
##     print '-'*50
##     print u'查询从行知路到大华三路'
##     print '\n'.join(g.find_path(u'行知路', u'大华三路'))
##     print '-'*50
##     print u'查询从南京东路到上海火车站'
##     print '\n'.join(g.find_shortest_path(u'南京东路', u'上海火车站'))
##     print '-'*50
##     print u'查询从肇家浜路到江苏路'
## #    print '\n'.join(g.find_path(u'肇家浜路', u'江苏路'))
##     print '-'*50
##     print u'从大华三路到上海火车站'
##     #print '\n'.join(g.find_shortest_path(u'大华三路', u'上海火车站'))
##     print '-'*50
##     print u'从大华三路漫步n站'
##     paths = g.wander(u'大华三路', 10)
##     #print '\n'.join(['->'.join([o.ljust(8) for o in e])+"   time: "+str(g.calculate_travel_time(e) for e in paths])
##     for e in paths:
##         print '->'.join([o.ljust(8) for o in e])
##         #print u"路程：%s公里, 所需时间: %s 分钟" % (g.calculate_distance(e)/1000, g.calculate_travel_time(e)/60)
    


