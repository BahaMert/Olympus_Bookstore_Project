import 'dart:convert';

import 'package:bookstore/utils/colors.dart';
import 'package:bookstore/utils/dimensions.dart';
import 'package:bookstore/utils/styles.dart';
import 'package:bookstore/views/action_bar.dart';
import 'package:bookstore/views/product_preview.dart';
import 'package:bookstore/views/slider.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../views/nav_draw.dart';


class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  void getUser() async {
    final url = Uri.parse("http://10.0.2.2:8000/all_books");

    final response = await http.get(
      Uri.https(url.authority, url.path),
      headers: <String, String>{
        "Accept": "application/json",
        "Content-Type": "charset=UTF-8",
      },


    );
    var responseList = jsonDecode(response.body) as List;
    print(responseList);

  }


  //Categories
  static final _categories = [
    "Reccomerndations",
    "Best Seller",
    "SELLL OF",
    "something bla bla"

  ];
  static int _currentCategory = 0;




  //DropDown



  //ProductPreview
  static final productPreviewList = <Product>[
    Product(
        pid: "5",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
      desc :"No Description",
      category : "Games",
      tag : "All",),
    Product(
        pid: "6",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
      desc :"No Description",
      category : "Games",
      tag : "All",),

    Product(
        pid: "4",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
        desc :"No Description",
       category : "Games",
       tag : "All",),

    Product(
        pid: "3",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
      desc :"No Description",
      category : "Games",
      tag : "All",),
    Product(
        pid: "2",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
      desc :"No Description",
      category : "Games",
      tag : "All",),
    Product(
        pid: "1",
        url:
        "https://d3o2e4jr3mxnm3.cloudfront.net/Mens-Jake-Guitar-Vintage-Crusher-Tee_68382_1_lg.png",
        productName: "Book name",
        rating: 3.7,
        price: 24.99,
        oldPrice: 20.00,
        stocks: 30,
        seller: "Seller1",
  desc :"No Description",
  category : "Games",
  tag : "All",),
];


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: nav_draw(),
      appBar: ActionBar(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Row(children: [
              Expanded(child: TextFormField()),
              IconButton(onPressed: () async {
                print("a");
                var data = {};
                print("a");
                final URL = Uri.parse("http://10.0.2.2:5000/all_books");//10.0.2.2  10.50.12.21
                print("aaaaaaaaa");

                var response = await http.post(URL,  body:data);
                print("aaaaaaaaa");
                if (response.statusCode == 200) {
                  print(response.body);
                } else {
                  print('A network error occurred');
                }


              }, icon: Icon(Icons.search))
            ]),
            SizedBox(
              height: 60,
              child: ListView(
                scrollDirection: Axis.horizontal,
                children: List.generate(_categories.length, (int index) {
                  return OutlinedButton(
                    onPressed: () {


                    },
                    child: Container(
                      height: 50.0,
                      child: Text(_categories[index]),
                    ),
                  );
                }),
              ),
            ),
            
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Padding(
                padding: Dimen.regularPadding,
                child: Row(
                  children: List.generate(
                      productPreviewList.length,
                          (index) => Row(children: [
                            ProductPreview(product: productPreviewList[index],),
                        SizedBox(width: 8)
                      ])),
                ),
              ),
            ),
            Text(
              "Recommendations",
              style: kHeadingTextStyle,
            ),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Padding(
                padding: Dimen.regularPadding,
                child: Row(
                  children: List.generate(
                      productPreviewList.length,
                          (index) => Row(children: [
                        ProductPreview(product: productPreviewList[index]),
                        SizedBox(width: 8)
                      ])),
                ),
              ),
            ),
          slider(),
            //Book of the Day


          ],

        ),
      ),
    );
  }
}