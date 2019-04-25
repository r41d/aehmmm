using Gtk;

int main(string[] args) {
	var count = 0;

	Gtk.init(ref args);

	var window = new Window();
	window.title = "Ähmmm...";
	window.border_width = 10;
	window.window_position = WindowPosition.CENTER;
	window.set_default_size(350, 70);
	window.destroy.connect(Gtk.main_quit);

	var label = new Label(count.to_string());

	var button = new Button.with_label("Ähmmm...");
	button.clicked.connect(() => {
		count++;
		label.set_text(count.to_string());
	});
	
	var obenunten = new Paned(Gtk.Orientation.VERTICAL);
	obenunten.add1(label);
	obenunten.add2(button);

	window.add(obenunten);
	window.show_all();

	Gtk.main();
	return 0;
}

