import { writable } from "svelte/store";
 
export class Message {
  constructor(type, text) {
    this.type = type;
    this.text = text;
    this.created = Date.now();
  }
}

export const messages = writable(new Array());

export const addMessage = (type, text) => {
    messages.update(messages => [...messages, new Message(type, text)]);
}