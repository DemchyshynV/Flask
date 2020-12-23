import {Component, OnInit} from '@angular/core';
import {ProductService} from './services/product.service';
import {IProduct} from './interfaces/product.interface';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  products: IProduct[];

  constructor(private productService: ProductService) {
  }

  ngOnInit(): void {
    this.productService.getAll().subscribe(value => this.products = value);
  }

  del(id: number): void {
    this.productService.del_by_id(id).subscribe();
    this.ngOnInit();
  }
}
