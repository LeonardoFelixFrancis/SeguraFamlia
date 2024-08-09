import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PersonService {

  constructor(private httpClient:HttpClient) { }

  getCurrentUser(): Observable<any> {
    return this.httpClient.get('http://localhost:8000/api/person/');
  }
    
}
