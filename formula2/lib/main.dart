import 'package:flutter/material.dart';
import 'widgets/custom_tab_bar.dart';
import 'package:flutter/src/widgets/editable_text.dart';


import 'package:http/http.dart' as http;

main() {
  runApp(MaterialApp(
    home: MyApp(),
  ));
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  
  late final TextEditingController _controller;

  TextStyle _bodytextstyle =
      TextStyle(fontSize: 40, fontWeight: FontWeight.bold);
  var pricebuttonpapdding = MaterialStateProperty.all(
      EdgeInsets.symmetric(horizontal: 50, vertical: 25));

  
//  Future<http.Response> fetchData() {
//    final response = await http.get('http://127.0.0.1:8000/getEUSAMeta?name=rosbag2_2022_07_10-10_01_59');
//    return  Map<String, dynamic> data = json.decode(response.body);
//}
//

  String _text = "initial";
  TextEditingController _c = new TextEditingController();

  void initState() {
    _c = new TextEditingController();
    super.initState();
  }
  

  @override
  void dispose(){
   _c?.dispose();
   super.dispose();
  }
  

  @override
  Widget build(BuildContext context) {
    String _email;
    double _metal;
    double _total;
    print('hello');
    return Scaffold(
      backgroundColor: Colors.white,
      body: ListView(
        children: [
          Column(
            children: [
              MediaQuery.of(context).size.width > 720
                  ? MyCustomAppbar()
                  : Container(
                      
                      height: 80,
                      width: double.infinity,
                      decoration: BoxDecoration(
                          color: Colors.black,
                          border: Border.all(color: Colors.black, width: 2)),
                      child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Image.network(
                                'assets/images/formulaImage.png',
                                width: MediaQuery.of(context).size.width * 0.5,
                            ),
                          ])),
            ],
          ),
          Container(
                      padding: EdgeInsets.symmetric(horizontal: 30),
                      margin:
                          EdgeInsets.symmetric(vertical: 10, horizontal: 60),
                      height: 80,
                      width: double.infinity,
                      
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                             "Formula 1 Students Database",
                             style: _bodytextstyle,
                           ),
                            
                          
                          ])),
          
          
          Container(
                      padding: EdgeInsets.symmetric(horizontal: 30),
                      margin:
                          EdgeInsets.symmetric(vertical: 20, horizontal: 60),
                      height: 80,
                      width: double.infinity,
                      decoration: BoxDecoration(
                          color: Colors.white,
                          border: Border.all(color: Colors.black, width: 2),
                          borderRadius: BorderRadius.circular(40)),
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            new TextField(
                            keyboardType: TextInputType.text,
                            onChanged: (v)=>setState((){_text=v;}),
                            controller: _c,

                          ),
                          new TextButton(
                            child: new Text("Submit"),
                            onPressed: (){
                              print(_c.text);
                              print("something");
                            },
                          ),
                          ])),
          
          

          

          
        ],
        
        
      ),
      
    );
    
  }

  
}