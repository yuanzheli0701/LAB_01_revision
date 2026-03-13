#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
    int id;
    int uid;
    char txt[100];
    int t;
    int l, c, s;
    int score;
    struct node* nxt;
};

struct pq {
    struct node* h;
};

void add(struct pq* q, int id, int uid, char* txt, int t, int l, int c, int s) {
    struct node* nn = (struct node*)malloc(sizeof(struct node));
    nn->id = id;
    nn->uid = uid;
    strcpy(nn->txt, txt);
    nn->t = t;
    nn->l = l;
    nn->c = c;
    nn->s = s;
    nn->score = (l * 1) + (c * 2) + (s * 3); 
    nn->nxt = NULL;

    if (q->h == NULL || nn->score > q->h->score) {
        nn->nxt = q->h;
        q->h = nn;
    } else {
        struct node* temp = q->h;
        while (temp->nxt != NULL && temp->nxt->score >= nn->score) {
            temp = temp->nxt;
        }
        nn->nxt = temp->nxt;
        temp->nxt = nn;
    }
}

void up(struct pq* q, int id, int nl, int nc, int ns) {
    struct node *curr = q->h, *prev = NULL;
    while (curr != NULL && curr->id != id) {
        prev = curr;
        curr = curr->nxt;
    }
    if (curr != NULL) {
        if (prev == NULL) q->h = curr->nxt;
        else prev->nxt = curr->nxt;
        
        int tid = curr->id, tuid = curr->uid, tt = curr->t;
        char ttxt[100]; strcpy(ttxt, curr->txt);
        int fl = curr->l + nl, fc = curr->c + nc, fs = curr->s + ns;
        free(curr);
        add(q, tid, tuid, ttxt, tt, fl, fc, fs); 
    }
}

void dec(struct pq* q, int limit) {
    struct pq tmp = {NULL};
    struct node* curr = q->h;
    while (curr != NULL) {
        struct node* nxt = curr->nxt;
        if (curr->t < limit) curr->score *= 0.8; 
        
        struct node* nn = curr;
        nn->nxt = NULL;
        if (tmp.h == NULL || nn->score > tmp.h->score) {
            nn->nxt = tmp.h;
            tmp.h = nn;
        } else {
            struct node* t2 = tmp.h;
            while (t2->nxt != NULL && t2->nxt->score >= nn->score) t2 = t2->nxt;
            nn->nxt = t2->nxt;
            t2->nxt = nn;
        }
        curr = nxt;
    }
    q->h = tmp.h;
}

void show(struct pq* q) {
    struct node* t = q->h;
    while (t) {
        printf("[%d: %d] -> ", t->id, t->score);
        t = t->nxt;
    }
    printf("NULL\n");
}

int main() {
    struct pq q = {NULL};
    add(&q, 1, 101, "p1", 10, 82, 0, 0);
    add(&q, 2, 102, "p2", 15, 47, 0, 0);
    add(&q, 3, 103, "p3", 5, 95, 0, 0);
    show(&q);
    
    up(&q, 2, 10, 0, 0);
    show(&q);
    
    dec(&q, 8);
    show(&q);
    
    return 0;
}
