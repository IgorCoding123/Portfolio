import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'portfolio';

  // Outer Accordion state
  activeAccordion = 'c';

  // Inner Tabs state
  activeTab = 'langC';

  toggleAccordion(section: string) {
    if (this.activeAccordion === section) {
      this.activeAccordion = '';
    } else {
      this.activeAccordion = section;
    }
  }
}
