#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <iostream>
#include <stdexcept>
#include <map>

#include <TMVA/Reader.h>

using namespace std;

class TMVAfillerOTF : public multidraw::TTreeFunction {
    public:
        TMVAfillerOTF(string variables_file, string xml_file); 
    
        char const* getName() const override { 
            return "TMVAfillerOTF"; 
        }
        TTreeFunction* clone() const override { 
            return new TMVAfillerOTF(var_file, XMLfile);
        }
    
        unsigned getNdata() override { return 1; }
        double evaluate(unsigned) override;
    
    protected:  
        ~TMVAfillerOTF();
        void bindTree_(multidraw::FunctionLibrary&) override;
    
        string XMLfile;
        string var_file;
        vector<string> variables;
        map<string, FloatArrayReader*> AReaderMap;
        map<string, float> FloatMap;
        TMVA::Reader *reader = new TMVA::Reader();
};

TMVAfillerOTF::TMVAfillerOTF(string variables_file, string xml_file): 
    TTreeFunction(), 
    var_file(variables_file),
    XMLfile(xml_file) 
{
    // Read variables from file, order is important!   
    string line;
    ifstream myfile (var_file);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            variables.push_back (line);
        }
        myfile.close();
    }
    else cout << "Unable to open " << var_file << endl;

    // Book FloatArrayReader for each variable  
    cout << "Found variables: " << endl;
    for (auto var: variables){
        string name(var);
        FloatArrayReader *areader{};
        float a = 0;
        AReaderMap.insert ( pair<string, FloatArrayReader*>(name,areader));
        FloatMap.insert ( pair<string, float>(name,a));
        cout << var << endl;
    }
}


double
TMVAfillerOTF::evaluate(unsigned)
{
    //cout << "Variables: ";
    //vector<float> tmp;
    for (auto var: variables){
        string name(var);
        FloatMap[name] = AReaderMap[name]->At(0);
        //cout << name << " = "<< FloatMap[name] << ", ";
        //tmp.push_back(FloatMap[name]);
    }
    //cout << endl;
    //cout << "Evaluate MVA: " << reader->EvaluateMVA("BDT") << endl;
    //cout << "Evaluate MVA2: " << reader->EvaluateMVA(tmp, "BDT") << endl;
    return reader->EvaluateMVA("BDT");
}

void
TMVAfillerOTF::bindTree_(multidraw::FunctionLibrary& _library)
{   
    for (auto var: variables){
        string name(var);
        _library.bindBranch(AReaderMap[name], var.c_str());
        reader->AddVariable( name, &FloatMap[name]);
        //reader->AddVariable( name, AReaderMap[name]->At(0));
    }
    
    reader->BookMVA( "BDT", XMLfile);
}

TMVAfillerOTF::~TMVAfillerOTF(){
    for (auto var: variables){
        string name(var);
        AReaderMap[name]=nullptr;
    }
}
