import { Component, Input } from '@angular/core';

@Component({
  selector: 'square',
  templateUrl: './square.component.html',
  styleUrl: './square.component.css'
})
export class SquareComponent {
  // "TOGGLE" - either u did it today or u didnt
  // "VALUE" - input a value like pages read
  @Input() type: string;

  private value: number = 0;

  public open() {
    
  }

}
