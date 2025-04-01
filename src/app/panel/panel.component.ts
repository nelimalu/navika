import { Component, Input } from '@angular/core';
import { SquareComponent } from '../square/square.component';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'panel',
  templateUrl: './panel.component.html',
  styleUrl: './panel.component.css'
})
export class PanelComponent {
  @Input() id: string;

  public loaded: boolean = false;
  public object: Object = Object;
  
  public data: any = [];
  public keys: any = [];
  public title: string = '';
  public subtitle: string = '';
  public colour: string = 'white'; 

  constructor(private http: HttpClient) {
      let request = this.http.get('http://127.0.0.1:8000/get-data')
        .subscribe(
          (response: any) => {
            this.data = response[this.id];
            this.title = response[this.id].title;
            this.subtitle = response[this.id].subtitle;
            this.colour = response[this.id].colour;
            this.loaded = true;
            console.log(this.data);
            this.keys = Object.keys(this.data.weekdays);

          }
        );
  }


  public squares: number[][] = [
    ...[...Array(7).keys()].map(() => [...Array(52).keys()])
  ];
}
