class Event:
    def __init__(self, event_id="", name="", date="", ticket_price=0.0, total_tickets=100, sold_tickets=0):
        self.event_id=event_id
        self.name=name
        self.date=date
        self.ticket_price=ticket_price
        self.total_tickets=total_tickets
        self.sold_tickets=sold_tickets

    def remaining_tickets(self):
        return max(0, self.total_tickets-self.sold_tickets)

    def occupancy_rate(self):
        if self.total_tickets==0:
            return 0.0
        return (self.sold_tickets/self.total_tickets)*100.0

    def revenue(self):
        return self.sold_tickets*self.ticket_price


class EventOrganizer:
    def __init__(self):
        self.events=[]

    def add_event(self, event):
        self.events.append(event)

    def sell_ticket(self, event_id, quantity=1):
        if quantity<=0:
            print("So luong ve mua phai > 0!")
            return False
        for ev in self.events:
            if ev.event_id==event_id:
                if ev.remaining_tickets()<quantity:
                    print(f"Ban ve that bai: Su kien '{ev.name}' chi con {ev.remaining_tickets()} ve, khong du dap ung {quantity} ve!")
                    return False
                ev.sold_tickets+=quantity
                print(f"Ban thanh cong {quantity} ve cho su kien '{ev.name}'. So ve con lai: {ev.remaining_tickets()}.")
                return True
        print(f"Khong tim thay su kien co ma {event_id}!")
        return False

    def calculate_event_revenue(self, event_id):
        for ev in self.events:
            if ev.event_id==event_id:
                return ev.revenue()
        return 0.0

    def display_active_events(self):
        print("\n" + "="*70)
        print(f"{'DANH SACH SU KIEN DANG DIEN RA':^70}")
        print("="*70)
        print(f"{'Ma SK':<8}{'Ten su kien':<26}{'Ngay':<12}{'Da ban/Tong':>12}{'Ty le':>10}")
        print("-"*70)
        for ev in self.events:
            tickets_info=f"{ev.sold_tickets}/{ev.total_tickets}"
            print(f"{ev.event_id:<8}{ev.name:<26}{ev.date:<12}{tickets_info:>12}{ev.occupancy_rate():>9.1f}%")
        print("="*70)


def main():
    org=EventOrganizer()
    org.add_event(Event("EV01", "Live Concert Vu Diep", "15/10/2026", 500000, total_tickets=50))
    org.add_event(Event("EV02", "Hoi thao AI & Data", "20/10/2026", 150000, total_tickets=100))
    org.add_event(Event("EV03", "Dem nhac Acoustic", "25/10/2026", 100000, total_tickets=30))

    org.display_active_events()

    print("\n--- THUC HIEN BAN VE ---")
    org.sell_ticket("EV01", 35)
    org.sell_ticket("EV01", 20) # Thu mua vuot qua so ve con lai
    org.sell_ticket("EV02", 80)

    org.display_active_events()

    rev_ev01=org.calculate_event_revenue("EV01")
    print(f"\n=> Doanh thu thuc te su kien EV01: {rev_ev01:,.0f} VND")


if __name__=="__main__":
    main()
