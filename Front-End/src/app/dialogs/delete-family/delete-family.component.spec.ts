import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteFamilyComponent } from './delete-family.component';

describe('DeleteFamilyComponent', () => {
  let component: DeleteFamilyComponent;
  let fixture: ComponentFixture<DeleteFamilyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DeleteFamilyComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteFamilyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
