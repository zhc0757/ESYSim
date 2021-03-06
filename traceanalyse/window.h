
#include <vector>
#include <string>
#include <iostream>

#include "esy_interdata.h"
#include "esy_argument.h"
#include "esy_linktool.h"

using namespace std;

#include "esy_eventtype.h"

class WindowAnalyser
{
private:
    EsyDataFileOStream< EsyDataItemTrafficWindow > * mp_windowout;
    vector< EsyDataItemTrafficWindow > m_window_list;
    long m_window_count;
    long m_window_width;
    long m_window_step;
    long m_router_num;

public:
    WindowAnalyser(long buffer_size, const string & path_file, long router_num, 
                   long window_width, long window_step);
    void analyse(const EsyDataItemEventtrace & item);
    void finish();
};
