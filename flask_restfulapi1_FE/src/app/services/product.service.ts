import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {IProduct} from '../interfaces/product.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private httpClient: HttpClient) {
  }

  getAll(): Observable<IProduct[]> {
    return this.httpClient.get<IProduct[]>('http://localhost:5000/product');
  }

  del_by_id(productId: number): Observable<void> {
    return this.httpClient.delete<void>(`http://localhost:5000/product/${productId}`);
  }
}
