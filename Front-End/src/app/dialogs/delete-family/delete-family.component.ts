import { Component, inject, Input  } from '@angular/core';
import { FormsModule, FormControl, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogActions, MatDialogClose, MatDialogTitle, MatDialogContainer, MatDialogModule, MatDialogContent, MatDialogRef } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FamilyService } from '../../core/services/family.service';


@Component({
  selector: 'app-delete-family',
  standalone: true,
  imports: [MatButtonModule, MatDialogTitle, MatDialogContent, MatDialogActions, MatDialogClose],
  templateUrl: './delete-family.component.html',
  styleUrl: './delete-family.component.css'
})
export class DeleteFamilyComponent {

  @Input() family_id!: number;

  constructor(
    private dialogRef: MatDialogRef<DeleteFamilyComponent>,
    private family_service: FamilyService
  ) { }



  cancel() {
    this.dialogRef.close();
  }

  delete(){
    this.family_service.delete(this.family_id).subscribe(() => {
      this.dialogRef.close();
    });
  }

}
