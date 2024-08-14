import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Person } from '../models/person_model';

@Injectable({
  providedIn: 'root',
})
export class PersonService {

  constructor(private httpClient:HttpClient) { }

  getCurrentUser(): Observable<any> {
    return this.httpClient.get('http://localhost:8000/api/person/');
  }

  update(data:Person): Observable<any> {
    return this.httpClient.put('http://localhost:8000/api/person/', data);
  }
    
}
