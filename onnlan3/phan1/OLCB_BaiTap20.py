class SupportTicket:
    def __init__(self, ticket_id="", customer_name="", issue="", priority="Medium", status="Open"):
        self.ticket_id=ticket_id
        self.customer_name=customer_name
        self.issue=issue
        # Do uu tien: 'High', 'Medium', 'Low'
        self.priority=priority if priority in ['High', 'Medium', 'Low'] else 'Medium'
        # Trang thai: 'Open', 'In Progress', 'Resolved', 'Closed'
        self.status=status

    def display(self):
        print(f"[{self.ticket_id}] Khach: {self.customer_name:<18} | Uu tien: {self.priority:<8} | Trang thai: {self.status:<12} | Yeu cau: {self.issue}")


class TicketManager:
    def __init__(self):
        self.tickets=[]

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"Tiep nhan ticket [{ticket.ticket_id}] thanh cong tu khach hang {ticket.customer_name}.")

    def process_next_ticket(self):
        # Tim cac ticket chua xu ly (Open hoac In Progress)
        pending=[t for t in self.tickets if t.status in ['Open', 'In Progress']]
        if not pending:
            print("Khong co ticket nao can xu ly.")
            return None

        # Thu tu uu tien: High (1) -> Medium (2) -> Low (3)
        priority_order={'High': 1, 'Medium': 2, 'Low': 3}
        pending.sort(key=lambda t: priority_order.get(t.priority, 4))
        
        target_ticket=pending[0]
        target_ticket.status="In Progress"
        print(f"\n[DANG XU LY TICKET UU TIEN CAO NHAT]:")
        target_ticket.display()
        return target_ticket

    def update_status(self, ticket_id, new_status):
        for t in self.tickets:
            if t.ticket_id==ticket_id:
                t.status=new_status
                print(f"Cap nhat trang thai ticket [{ticket_id}] thanh '{new_status}' thanh cong.")
                return True
        print(f"Khong tim thay ticket co ma {ticket_id}!")
        return False

    def show_pending_tickets(self):
        print("\n" + "="*70)
        print(f"{'DANH SACH TICKET DANG CHO XU LY (PENDING)':^70}")
        print("="*70)
        pending=[t for t in self.tickets if t.status in ['Open', 'In Progress']]
        if not pending:
            print("Tat ca ticket deu da duoc xu ly hoan tat.")
        else:
            for t in pending:
                t.display()
        print("="*70)


def main():
    tm=TicketManager()
    t1=SupportTicket("TK01", "Nguyen Van An", "Quen mat khau tai khoan", "Low")
    t2=SupportTicket("TK02", "Cong ty TNHH ABC", "Loi thanh toan don hang gap", "High")
    t3=SupportTicket("TK03", "Tran Thi Mai", "Giao dien tren app bi loi font", "Medium")
    t4=SupportTicket("TK04", "VIP Le Van Long", "He thong may chu bi mat ket noi", "High")

    print("--- TIEP NHAN CAC TICKET ---")
    tm.add_ticket(t1)
    tm.add_ticket(t2)
    tm.add_ticket(t3)
    tm.add_ticket(t4)

    tm.show_pending_tickets()

    # Tu dong xu ly ticket co do uu tien cao nhat
    processed1=tm.process_next_ticket()
    if processed1:
        tm.update_status(processed1.ticket_id, "Resolved")

    processed2=tm.process_next_ticket()

    tm.show_pending_tickets()


if __name__=="__main__":
    main()
