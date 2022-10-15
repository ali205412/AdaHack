import 'package:flutter/material.dart';

class MyCustomAppbar extends StatefulWidget {
  const MyCustomAppbar({Key? key}) : super(key: key);

  @override
  State<MyCustomAppbar> createState() => _MyCustomAppbarState();
}

class _MyCustomAppbarState extends State<MyCustomAppbar> {
  @override
  Widget build(BuildContext context) {
    return Container(
            height: 100,
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
              ]
                
    )
    );
  }
}