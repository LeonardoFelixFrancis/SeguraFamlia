import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Family } from '../models/family_model';

@Injectable({
  providedIn: 'root',
})
export class FamilyService {

  constructor(private httpClient:HttpClient) { }

  create(data: Family): Observable<any> {
    return this.httpClient.post('http://localhost:8000/api/family/', data);
  }

  get(): Observable<any> {
    return this.httpClient.get('http://localhost:8000/api/family/get-user-family/');
  }
    
  delete(id: number): Observable<any> {
    return this.httpClient.delete(`http://localhost:8000/api/family/${id}/`);
  }

  
}
